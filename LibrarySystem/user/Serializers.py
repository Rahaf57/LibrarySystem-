from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ['id', 'gender', 'gender_persian']


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'role', 'role_persian']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city', 'city_persian']


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'faculty', 'faculty_persian']


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ['id', 'semester', 'semester_persian']

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ['id', 'email', 'username', 'password']


   extra_kwargs = {'password': {'write_only': True}}


   def create(self, validated_data):
       user = User(
           username=validated_data['username'],
           email=validated_data['email'],
       )
       user.set_password(validated_data['password'])
       user.save()
       return user



class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['user', 'first_name', 'last_name']

class DespositesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desposites
        fields = ['id', 'user', 'copy', 'issue_date', 'due_date']


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ['id', 'news_title', 'news_summary', 'news_details', 'news_ref',
                  'news_title_persion', 'news_summary_presion', 'news_details_prsion', 'news_ref_persion',
                  'news_date', 'faculty']


class ChangePasswordSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)