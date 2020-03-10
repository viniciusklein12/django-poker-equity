from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Card, Hand, Flop
from .serializers import HandSerializer, CardSerializer, FlopSerializer


class HandList(APIView):

    def get(self, request):
        hands = Hand.objects.all()
        serializer = HandSerializer(hands, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HandSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class HandDetail(APIView):

    def get_object(self, pk):
        try:
            return Hand.objects.get(pk=pk)
        except Hand.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        hand = self.get_object(pk)
        serializer = HandSerializer(hand)
        return Response(serializer.data)

    def put(self, request, pk):
        hand = self.get_object(pk)
        serializer = HandSerializer(hand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        hand = self.get_object(pk)
        hand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        hand = self.get_object(pk)
        serializer = HandSerializer(hand, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FlopList(APIView):

    def get(self, request):
        flops = Flop.objects.all()
        serializer = FlopSerializer(flops, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlopSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FlopDetail(APIView):

    def get_object(self, pk):
        try:
            return Flop.objects.get(pk=pk)
        except Flop.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        flop = self.get_object(pk)
        serializer = FlopSerializer(flop)
        return Response(serializer.data)

    def put(self, request, pk):
        flop = self.get_object(pk)
        serializer = FlopSerializer(flop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        flop = self.get_object(pk)
        flop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        flop = self.get_object(pk)
        serializer = FlopSerializer(flop, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HandCardsAPIView(generics.ListAPIView):
    serializer_class = CardSerializer
    def get_queryset(self):
        return Card.objects.filter(hand=self.kwargs.get('pk'))

class FlopCardsAPIView(generics.ListAPIView):
    serializer_class = CardSerializer
    def get_queryset(self):
        return Card.objects.filter(flop=self.kwargs.get('pk'))
