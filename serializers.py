from rest_framework import serializers
from musterroll.models import Roles
from login.models import EmployeeDropdown


class RoleNameSerializer(serializers.ModelSerializer):
	class Meta:
		model = EmployeeDropdown
		fields= ('value',)

class RolesSerializer(serializers.ModelSerializer):
	roles=RoleNameSerializer(required=False, allow_null=True,read_only=True)
	class Meta:
	    model = Roles
	    fields = ('roles',)


