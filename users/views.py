from django.shortcuts import render
from django.urls import path
from rest_framework import generics
from rest_framework.response import Response

from users.models import *
from users.serializers import PassengerSerializer
# Create your views here.


class checkout (generics.CreateAPIView):
        def post(self, request, *args, **kwargs):
            id = request.data['id']
           
            pas =Passenger.objects.get(card = id)

            travel = Captine.objects.get(id=1).travel

            pas.funds = pas.funds - travel.price 
            pas.save()

            bus = Bus.objects.create( travel = travel , captine =Captine.objects.get(id=1))

            bus.save()
            bus.passenger.add(pas)
            return Response(pas.funds)
        

class add (generics.CreateAPIView):
      def post(self, request, *args, **kwargs): 
        id = request.data['id']
        amount = request.data['amount']
        pas =Passenger.objects.get(card = id)
        pas.funds = pas.funds + int(amount)
        pas.save()
        return Response(pas.funds)
      

class new (generics.CreateAPIView) :
     def post(self, request, *args, **kwargs):
          pass
          


class pass_info(generics.CreateAPIView) :
     serializer_class  = PassengerSerializer
     def post(self, request, *args, **kwargs): 
        id = request.data['id']
        pas =Passenger.objects.get(card = id)
        return Response(PassengerSerializer(pas).data)


class pass_info_test(generics.CreateAPIView) :
     serializer_class  = PassengerSerializer
     def post(self, request, *args, **kwargs): 
        id = request.data['id']
        pas =Passenger.objects.get(card = id)
        return Response(PassengerSerializer(pas).data)

        



