from rest_framework import serializers
from main.models import *

class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    country = serializers.CharField()
    gender = serializers.ChoiceField(GENDER.choices)
    birthday = serializers.DateField()


