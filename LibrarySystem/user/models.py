from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# from Book.models import *


class Gender(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=30)
    gender_persian = models.CharField(max_length=30)

    def __str__(self):
        return f" {self.gender} "


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=50)
    role_persian = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.role} "


class City(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=80)
    city_persian = models.CharField(max_length=80)

    def __str__(self):
        return f" {self.city} "


class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    faculty = models.CharField(max_length=50)
    faculty_persian = models.CharField(max_length=50)

    def __str__(self):
        return f" {self.faculty} "


class Semester(models.Model):
    id = models.AutoField(primary_key=True)
    semester = models.CharField(max_length=30)
    semester_persian = models.CharField(max_length=30)

    def __str__(self):
        return f" {self.semester}  "


class User(AbstractUser):
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)




    def __str__(self):
        return f"  {self.username}   "


class UserAccount(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    identification_no = models.IntegerField()
    registration_no = models.IntegerField()
    contact_no = models.CharField(max_length=14)
    page_no = models.IntegerField()
    original_address = models.CharField(max_length=50)
    current_address = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    signature = models.CharField(max_length=255)

    def __str__(self):
        return f"  {self.first_name} - {self.last_name}  "



class Desposites(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    copy = models.ForeignKey('Book.Copies', on_delete=models.CASCADE)
    issue_date = models.DateField()
    due_date = models.DateField()

    def __str__(self):
        return f"  {self.issue_date} - {self.due_date} "


class New(models.Model):
    id = models.AutoField(primary_key=True)
    news_title = models.CharField(max_length=500)
    news_summary = models.TextField()
    news_details = models.TextField()
    news_ref = models.CharField(max_length=500)
    news_title_persion = models.CharField(max_length=500)
    news_summary_presion = models.TextField()
    news_details_prsion = models.TextField()
    news_ref_persion = models.CharField(max_length=500)
    news_date = models.DateField()
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null= True)

    def __str__(self):
        return f"  {self.news_title} - {self.news_summary} - {self.news_details} - {self.news_ref} - {self.faculty} "
