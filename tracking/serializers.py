from rest_framework import serializers
from tracking.models import *

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'date', 'duration', 'notes']

class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Me
        fields = ['id',"date",'weight','height','body_fat']

