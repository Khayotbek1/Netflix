from rest_framework import serializers
from main.models import *


# class ActorSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=True)
#     country = serializers.CharField()
#     gender = serializers.ChoiceField(GENDER.choices)
#     birthday = serializers.DateField()



class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
        read_only_fields = ('id',)
