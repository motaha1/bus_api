from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from users.models import *


class PassengerSerializer(ModelSerializer):
        class Meta:
            model = Passenger
            fields = '__all__'

class   TravelSerializer(ModelSerializer):
        class Meta:
            model = Travel
            fields = '__all__'
class   CapSerializer(ModelSerializer):
        travel= TravelSerializer()
        class Meta:
            model = Captine
            fields = '__all__'

class BusSerializer (ModelSerializer) : 
    #   passenger = PassengerSerializer()
      travel = TravelSerializer()
      captine = CapSerializer ()
      class Meta:
            model = Bus
            fields = '__all__'
       






