from django.db import models

# Create your models here.
class Card(models.Model):
    '''Card Model'''
    front = models.TextField()
    back = models.TextField()
    description = models.TextField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    video_link = models.URLField(null=True, blank=True)
    class Meta:
        ordering = ["id"]
        db_table = 'card'
        verbose_name = "flash card" 

    def __str__(self) -> str:
        return self.front + " | " + self.back

class Desk(models.Model):
    '''Desk Model'''
    name = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    description = models.TextField()
    cards = models.ManyToManyField(Card)
    class Meta:
        ordering = ["id"]
        db_table = 'desk'
        verbose_name = "desk card" 