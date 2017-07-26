# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .serializers import RolesSerializer
from .models import Roles,AuthUser,EmployeePrimdetail,Daksmsstatus
from datetime import datetime, timedelta
from rest_framework import status
from .service import get_random_number,send_sms
from django.utils import timezone
# Create your views here.

class LoginView(APIView):
	def post(self,request):
		username=request.data['username']
		password=request.data['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				roles = Roles.objects.filter(emp_id=username)
				serialized_roles=RolesSerializer(instance=roles, many=True).data
				all_roles=[]
				
				payload = {
				'message':"logged in",
            	'all_roles' : serialized_roles
            	}

            	for i in serialized_roles:
            		all_roles.append(i['roles']['value'])
            	request.session['roles']=all_roles
		return Response(payload)


class LogoutView(APIView):
	def get(self, request):
		logout(request)
		payload={
		'message':"logged out",
		}
		return Response(payload)


class GetOtpView(APIView):
    def post(self, request):
		pmail=request.data['user']
		phone_number = request.data['phone_number']

		matching = EmployeePrimdetail.objects.filter(mob=phone_number, emp_id=pmail).count()
		otp=''
		if matching:
			random_number = get_random_number()
			request.session['random_number']=random_number
			send_sms("OTP is " + str(random_number), phone_number=phone_number)
			entry={
				'phonenos':phone_number,
				'counttry':0,
				'otp': random_number,
				'rectimestamp': datetime.now(),
				'updatestatus' : 'Y'
			}
			#Daksmsstatus.objects.create(**entry)

			payload = {
				'message': 'Otp sent successfully.'
			}

			return Response(payload)
		else:
			payload = {
				'message': 'Phone Number not found.'
			}
			return Response(payload, status=status.HTTP_400_BAD_REQUEST)


class OtpConfirmationView(APIView):
	def post(self,request):
		print(request.session['random_number'])
		otp = request.data['otp']
		if otp == request.session['random_number']:
			payload={
						'message' : 'OTP Verification Successful'
					}

			return Response(payload)
		else:
			payload={
					'message' : 'Invalid OTP'
				}

			return Response(payload,status=status.HTTP_400_BAD_REQUEST)
			


class ChangePasswordView(APIView):
	def post(self, request):
		new_password = request.data['new_password']
		user_id = request.data['user']

		u = User.objects.get(username=user_id)
		u.set_password(new_password)
		u.save()

		payload = {
			'message': 'Password Changed'
		}

		return Response(payload)
