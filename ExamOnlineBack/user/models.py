from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.
class Group(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class GroupPermissions(models.Model):
    group = models.ForeignKey(Group, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

class User(models.Model):
    """User"""
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=False null=False)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user' 


class Clazz(models.Model):
    """Class"""
    year = models.CharField("grade", max_length=20)
    major = models.CharField("major", max_length=20)
    clazz = models.CharField("class", max_length=20)

    class Meta:
        ordering = ['id']
        verbose_name = "class"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.year + self.major + self.clazz


class Student(models.Model):
    """Student model class"""
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    name = models.CharField("Name", max_length=20, default="")
    # One -to -one association field
    user = models.OneToOneField(User, verbose_name="user", on_delete=models.CASCADE)
    gender = models.CharField("gender", max_length=1, choices=GENDER_CHOICES, default="")
    clazz = models.ForeignKey(Clazz, verbose_name="class", on_delete=models.CASCADE, default="1")


    class Meta:
        ordering = ['id']
        db_table = 'user_student'
        verbose_name = 'student'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    "Teacher model class "
    GENDER_CHOICES = (
        ('m', 'male'),
        ('f', 'female')
    )
    TITLE_CHOICES = (
       ('Lecturer', 'Lecturer'),
        ('Associate Professor', 'Associate Professor'),
        ('Professor', 'Professor')
    )
    name = models.CharField("Name", max_length=20, default="")
    gender = models.CharField("Gender", max_length=1, choices=GENDER_CHOICES, default="male")
    title = models.CharField("Job Title", max_length=20, choices=TITLE_CHOICES, default="lecturer")
    institute = models.CharField("College", max_length=20, default="")

    # One -to -one association field
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="用户")

    class Meta:
        ordering = ['id']
        db_table = 'user_teacher'
        verbose_name = 'teacher'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
