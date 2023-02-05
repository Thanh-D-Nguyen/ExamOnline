from django.db import models

# Create your models here.
class Card(models.Model):
    '''Card Model'''
    front = models.TextField()
    back = models.TextField()
    image = models.URLField(null=True, blank=True)
    videoLink = models.URLField(null=True, blank=True)

class Deck(models.Model):
    '''Desk Model'''
    name = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    description = models.TextField()
    cards = models.ManyToManyField(Card)