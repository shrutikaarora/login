# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    user_type = models.CharField(max_length=255)

    class Meta:
        managed=False
        db_table = 'auth_user'


class EmployeeDropdown(models.Model):
    sno = models.AutoField(db_column='Sno', primary_key=True)  # Field name made lowercase.
    pid = models.IntegerField(db_column='Pid', blank=True, null=True)  # Field name made lowercase.
    field = models.CharField(db_column='Field', max_length=500, blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'employee_dropdown'


class EmployeePrimdetail(models.Model):
    title = models.ForeignKey(EmployeeDropdown, related_name='title',db_column='Title', blank=True, null=True, limit_choices_to={'field':'TITLE'},on_delete=models.CASCADE)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dept = models.ForeignKey(EmployeeDropdown,db_column='Dept', related_name='department', blank=True, null=True, limit_choices_to={'field':'DEPARTMENT'},on_delete=models.CASCADE)  # Field name made lowercase.
    doj = models.DateField(db_column='DOJ', blank=True, null=True)  # Field name made lowercase.
    current_pos = models.ForeignKey(EmployeeDropdown, related_name='Current_Position',db_column='Current_Pos', blank=True, null=True,on_delete=models.CASCADE)  # Field name made lowercase.
    emp_type = models.ForeignKey(EmployeeDropdown, related_name='Emp_Type', blank=True,db_column='Emp_Type', null=True, limit_choices_to={'Field':'TYPE OF EMPLOYEMENT'},on_delete=models.CASCADE)  # Field name made lowercase.
    emp_category = models.ForeignKey(EmployeeDropdown, related_name='Emp_Category', blank=True, null=True,db_column='emp_category', limit_choices_to={'Field':'CATEGORY OF EMPLOYEE'},on_delete=models.CASCADE)  # Field name made lowercase.
    desg = models.ForeignKey(EmployeeDropdown, related_name='designation',db_column='Desg', blank=True, null=True, limit_choices_to={'Field':'DESIGNATION'},on_delete=models.CASCADE)  # Field name made lowercase.
    cadre = models.ForeignKey(EmployeeDropdown, related_name='cadre',db_column='Cadre', blank=True, null=True, limit_choices_to={'Field':'CADRE'},on_delete=models.CASCADE)  # Field name made lowercase.
    ladder = models.ForeignKey(EmployeeDropdown, related_name='ladder',db_column='Ladder', blank=True, null=True, limit_choices_to={'Field':'LADDER'},on_delete=models.CASCADE)  # Field name made lowercase.
    shift = models.ForeignKey(EmployeeDropdown, related_name='shift',db_column='Shift', blank=True, null=True, limit_choices_to={'Field':'SHIFT'},on_delete=models.CASCADE)  # Field name made lowercase.
    mob = models.CharField(db_column='Mob', max_length=12, blank=True, null=True)  # Field name made lowercase.
    mob1 = models.CharField(db_column='Mob1', max_length=12, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emp_id = models.ForeignKey(AuthUser,to_field='username',db_column='Emp_Id', primary_key=True,unique=True,on_delete=models.CASCADE)  # Field name made lowercase.
    lib_card_no = models.CharField(db_column='Lib_Card_No', max_length=15, blank=True, null=True)  # Field name made lowercase.
    organization = models.ForeignKey(EmployeeDropdown, related_name='organization', blank=True, null=True, limit_choices_to={'Field':'SHIFT'},on_delete=models.CASCADE,db_column='Organization')  # Field name made lowercase.
    emp_status = models.CharField(db_column='Emp_Status', max_length=255, blank=True, null=True, default='ACTIVE')  # Field name made lowercase.

    class Meta:
        db_table = 'employee_primdetail'


class Roles(models.Model):
    sno = models.AutoField(db_column='Sno', primary_key=True)  # Field name made lowercase.
    emp_id = models.ForeignKey(EmployeePrimdetail,db_column='Emp_Id', related_name='employee_id_role', max_length=20, on_delete=models.CASCADE)  # Field name made lowercase.
    roles = models.ForeignKey(EmployeeDropdown,db_column='roles', related_name='role', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'roles'



class Daksmsstatus(models.Model):
    phonenos = models.CharField(db_column='PhoneNos', max_length=100) 
    updatestatus = models.CharField(db_column='UpdateStatus', max_length=10) 
    rectimestamp = models.DateTimeField(db_column='RecTimeStamp')
    counttry = models.IntegerField(db_column='CountTry')
    msg = models.TextField(db_column='Msg') 
    otp = models.CharField(db_column='Otp',max_length=100, blank=True, null=True)
    senderid = models.IntegerField(db_column='SenderID', blank=True, null=True)
    sendby = models.CharField(db_column='Sendby', max_length=50, blank=True, null=True)
    mainid = models.AutoField(db_column='MainId', primary_key=True) 

    class Meta:
        db_table = 'daksmsstatus'
