from .models import Hand, Card, Flop
from rest_framework import serializers


class CardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Card

        fields = ['value', 'suit']

class HandSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)
    class Meta:
        model = Hand
        fields = ['id', 'cards']

class FlopSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)
    class Meta:
        model = Flop
        fields = ['id', 'cards']