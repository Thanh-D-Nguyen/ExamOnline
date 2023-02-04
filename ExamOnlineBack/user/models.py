from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.
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
