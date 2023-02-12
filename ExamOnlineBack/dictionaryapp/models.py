from django.db import models

# Create your models here.
class Example(models.Model):
    ref_id = models.IntegerField()
    content = models.TextField(null=True, blank=True)
    mean = models.TextField(null=True, blank=True)
    trans = models.TextField(null=True, blank=True)
    
    class Meta:
        ordering = ["id"]
        db_table = 'example'
        verbose_name = "Example"
        verbose_name_plural = verbose_name
        # app_label = 'dictionaryapp'

    def __str__(self):
        return "id: " + self.ref_id
    
    
class Grammar(models.Model):
    define = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    mean = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    level = models.CharField(max_length=100, null=True, blank=True)
    favorite = models.BooleanField(default=False)
    remember = models.BooleanField(default=False)
    category = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        ordering = ["id"]
        db_table = 'grammar'
        verbose_name = "Grammar"
        verbose_name_plural = verbose_name
        # app_label = 'dictionaryapp'

    def __str__(self):
        return self.define

class JaVi(models.Model):
    word = models.CharField(max_length=255, null=True, blank=True)
    phonetic = models.CharField(max_length=255, null=True, blank=True)
    mean = models.TextField(null=True, blank=True)
    seq = models.SmallIntegerField(null=True, blank=True)
    opposite = models.CharField(max_length=255, null=True, blank=True)
    favorite = models.BooleanField(default=False)
    synsets = models.CharField(max_length=255, null=True, blank=True)
    related = models.TextField(null=True, blank=True)
    pronunciation = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        ordering = ["id"]
        db_table = 'javi'
        verbose_name = "Japanese - Vietnamese"
        verbose_name_plural = verbose_name
        # app_label = 'dictionaryapp'

    def __str__(self):
        return self.word

class Kanji(models.Model):
    kanji = models.CharField(max_length=10)
    mean = models.CharField(max_length=150, blank=True, null=True)
    level = models.SmallIntegerField(null=True, blank=True)
    on = models.CharField(max_length=200, null=True, blank=True)
    kun = models.CharField(max_length=200, null=True, blank=True)
    svg = models.TextField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    short = models.CharField(max_length=10, blank=True, null=True)
    frequenty = models.IntegerField(null=True, blank=True)
    components = models.TextField(null=True, blank=True)
    stroke_count = models.SmallIntegerField(default=-1)
    components_detail = models.TextField(null=True, blank=True)
    examples = models.TextField(null=True, blank=True)
    favorite = models.BooleanField(default=False)
    remember = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["id"]
        db_table = 'kanji'
        verbose_name = "Kanji"
        verbose_name_plural = verbose_name
        # app_label = 'dictionaryapp'

    def __str__(self):
        return self.kanji
    
class ViJa(models.Model):
    word = models.CharField(max_length=255)
    kind = models.CharField(max_length=255, blank=True, null=True)
    mean = models.TextField(blank=True, null=True)
    favorite = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["id"]
        db_table = 'vija'
        verbose_name = "Vietnamese - Japanese"
        verbose_name_plural = verbose_name
        # app_label = 'dictionaryapp'

    def __str__(self):
        return self.word