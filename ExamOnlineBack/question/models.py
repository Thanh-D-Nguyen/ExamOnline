from django.db import models


# Create your models here.
class Choice(models.Model):
    """Selected Questions Model"""
    LEVEL_CHOICES = (
        ('1', 'Begin'),
        ('2', 'Simple'),
        ('3', 'Normal'),
        ('4', 'Difficult'),
        ('5', 'Expert')
    )
    ANSWER_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    )
    question = models.TextField("Question", default="")
    answer_A = models.CharField("Option A", max_length=200, default="")
    answer_B = models.CharField("Option B", max_length=200, default="")
    answer_C = models.CharField("Option C", max_length=200, default="")
    answer_D = models.CharField("Option D", max_length=200, default="")
    right_answer = models.CharField("Correct option", max_length=1, choices=ANSWER_CHOICES, default="A")
    analysis = models.TextField("Subject analysis", default="None for the time being")
    score = models.PositiveSmallIntegerField("Score", default=2)
    level = models.CharField("Difficulty level", max_length=1, choices=LEVEL_CHOICES, default='1')

    class Meta:
        ordering = ['id']
        verbose_name = 'Choice'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question


class Fill(models.Model):
    """Judgment question model"""
    LEVEL_CHOICES = (
        ('1', 'Begin'),
        ('2', 'Simple'),
        ('3', 'Normal'),
        ('4', 'Difficult'),
        ('5', 'Expert')
    )
    question = models.TextField("Question", default="")
    right_answer = models.CharField("Correct answer", max_length=200, default="")
    analysis = models.TextField("Subject analysis", default="None for the time being")
    score = models.PositiveSmallIntegerField("Score", default=2)
    level = models.CharField("Difficulty level", max_length=1, choices=LEVEL_CHOICES, default='1')

    class Meta:
        ordering = ['id']
        verbose_name = 'Blank'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question


class Judge(models.Model):
    """Judgment question model"""
    LEVEL_CHOICES = (
        ('1', 'Begin'),
        ('2', 'Simple'),
        ('3', 'Normal'),
        ('4', 'Difficult'),
        ('5', 'Expert')
    )
    ANSWER_CHOICES = (
        ('T', 'Correct'),
        ('F', 'Wrong')
    )
    question = models.TextField("Question", default="")
    right_answer = models.CharField("Correct answer", max_length=1, choices=ANSWER_CHOICES, default="T")
    analysis = models.TextField("Subject analysis", default="None for the time being")
    score = models.PositiveSmallIntegerField("Score", default=2)
    level = models.CharField("Difficulty level", max_length=1, choices=LEVEL_CHOICES, default='1')

    class Meta:
        ordering = ['id']
        verbose_name = 'True or False'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question


class Program(models.Model):
    """Programming question model"""
    LEVEL_CHOICES = (
        ('1', 'Begin'),
        ('2', 'Simple'),
        ('3', 'Normal'),
        ('4', 'Difficult'),
        ('5', 'Expert')
    )
    question = models.TextField("Question", max_length=200, default="")
    answer_template = models.TextField("Answer template", default="")
    test_case = models.TextField("Test case", default="")
    analysis = models.TextField("Subject analysis", default="")
    score = models.PositiveSmallIntegerField("Score", default=8)
    level = models.CharField("Difficulty level", max_length=1, choices=LEVEL_CHOICES, default='1')

    class Meta:
        ordering = ['id']
        verbose_name = 'Programming'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question