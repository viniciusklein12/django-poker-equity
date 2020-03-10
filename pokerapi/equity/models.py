from django.db import models

# Create your models here.

SUIT_CHOICES = [('D', 'Diamonds'),
    ('S', 'Spades'),
    ('H', 'Hearts'),
    ('C', 'Clubs')]

class Hand(models.Model):
    pass

class Flop(models.Model):
    pass

class Card(models.Model):
    value = models.CharField(max_length=1)
    suit = models.CharField(max_length=1, choices=SUIT_CHOICES, default='D')
    hand = models.ForeignKey('Hand', on_delete=models.CASCADE)
    flop = models.ForeignKey('Flop', on_delete=models.CASCADE)