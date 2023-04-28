from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from users.models import *


class PassengerSerializer(ModelSerializer):
        class Meta:
            model = Passenger
            fields = '__all__'


