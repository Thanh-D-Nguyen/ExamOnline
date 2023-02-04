from django.db import models
from question.models import Choice, Fill, Judge, Program
from user.models import Student, Clazz
from datetime import datetime
import random


# Create your models here.
class Paper(models.Model):
    """Test papers model"""
    LEVEL_CHOICES = (
        ('1', 'getting Started'),
        ('2', 'Simple'),
        ('3', 'usually'),
        ('4', 'More difficult'),
        ('5', 'difficulty')
    )
    name = models.CharField("Test paper name", max_length=20, default="")
    score = models.PositiveSmallIntegerField("Total score", default=100)
    choice_number = models.PositiveSmallIntegerField("Number of choice questions", default=10)
    fill_number = models.PositiveSmallIntegerField("Number of filling questions", default=10)
    judge_number = models.PositiveSmallIntegerField("Number of judgments", default=10)
    program_number = models.PositiveSmallIntegerField("Number of programming questions", default=5)
    level = models.CharField("Difficulty level", max_length=1, choices=LEVEL_CHOICES, default="1")

    class Meta:
        ordering = ["id"]
        verbose_name = "Test papers "
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.score = (self.choice_number + self.fill_number + self.judge_number) * 2 + self.program_number * 8
        super().save(*args, **kwargs)


class Exam(models.Model):
    """Test model class"""
    name = models.CharField("Test name", max_length=20, default="")
    exam_date = models.DateField("Test date", default="")
    total_time = models.PositiveSmallIntegerField("duration", default=120, help_text="Press the length and fill in the minute")
    paper = models.OneToOneField(Paper, on_delete=models.CASCADE, verbose_name="Test paper", default="")
    major = models.CharField("major", max_length=20, default="")
    tips = models.TextField("Candidates' notes", default="")
    clazzs = models.ManyToManyField(Clazz, verbose_name="Class to take the exam")

    class Meta:
        ordering = ["id"]
        db_table = 'exam_info'
        verbose_name = "take an exam"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Grade(models.Model):
    """Grade Model Category"""
    exam = models.ForeignKey(Exam, verbose_name="take an exam", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, verbose_name="student", on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField("Fraction", default="")
    create_time = models.DateTimeField("Creation date", auto_now_add=True)
    update_time = models.DateTimeField("Modify", auto_now=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'score'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.id}of{self.student}for{self.score}point'


class Practice(models.Model):
    """Simulation exercise"""
    name = models.CharField("Practice nametice name", max_length=20)
    student = models.ForeignKey(Student, verbose_name="student", on_delete=models.CASCADE)
    create_time = models.DateTimeField("Practice time", auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'practise'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = f'Simulation exercise{datetime.now().strftime("%Y%m%d")}{random.randint(1000, 9999)}'
        super().save(*args, **kwargs)
