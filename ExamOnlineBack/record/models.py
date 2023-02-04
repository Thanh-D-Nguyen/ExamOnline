from django.db import models

# Create your models here.
from exam.models import Practice
from question.models import Choice, Fill, Judge, Program
from user.models import Student


class Record(models.Model):
    """Practice record"""
    practice = models.ForeignKey(Practice, verbose_name="Practise", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, verbose_name="Student", on_delete=models.CASCADE)
    your_answer = models.TextField("Your answer", null=True, blank=True)

    class Meta:
        # Abstract class
        abstract = True

    def __str__(self):
        return self.your_answer


class ChoiceRecord(Record):
    """Selected Questions Answer Record"""
    choice = models.ForeignKey(Choice, verbose_name="Choice", on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = 'Selected Questions Answer Record'
        verbose_name_plural = verbose_name


class FillRecord(Record):
    """Fill in the blank questions and answer records"""
    fill = models.ForeignKey(Fill, verbose_name="Blank", on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = 'Fill in the blank questions and answer records'
        verbose_name_plural = verbose_name


class JudgeRecord(Record):
    judge = models.ForeignKey(Judge, verbose_name="True or False", on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = 'Judgment question answer record'
        verbose_name_plural = verbose_name


class ProgramRecord(Record):
    program = models.ForeignKey(Program, verbose_name="Programming", on_delete=models.CASCADE)
    cmd_msg = models.TextField("输出结果", null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Programming Questions Answer Record'
        verbose_name_plural = verbose_name
