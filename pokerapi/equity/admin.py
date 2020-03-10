from django.contrib import admin
from .models import Hand, Flop, Card
# Register your models here.

admin.site.register(Hand)
admin.site.register(Flop)
admin.site.register(Card)