from django.db import models
from datetime import datetime

# Create your models here.
class AppUser(models.Model):
    full_name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    usertype = models.CharField(max_length=200)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "app_user"
class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20)

    class Meta:
        db_table= "app_courses"

class Student(models.Model):
    first_name = models.CharField(max_length= 100)
    middle_name = models.CharField(max_length=100, null = True, blank = True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=100)
    academic_level = models.CharField(max_length=100)
    academic_status = models.CharField(max_length=100)
    acdemic_org = models.CharField(max_length=100)
    academic_skill = models.CharField(max_length=200, null = True, blank = True)
    # course = model.models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    course = models.ForeignKey( Course, on_delete=models.CASCADE)
    intake = models.CharField(max_length=100, null=True, blank=True)
    shift = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.CharField(max_length=200)
    visisted_at = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = "app_students"

