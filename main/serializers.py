from rest_framework import serializers
from datetime import datetime
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

    def validate_name(self, name):
        if len(name) < 3:
            raise serializers.ValidationError('Name must be at least 3 characters long')
        return name

    def validate_birthday(self, birthday):
        if str(birthday) > str(datetime.today()):
            raise serializers.ValidationError('Birthday must not be in the future')
        return birthday



class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        read_only_fields = ('id',)


class ActorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name',)
        read_only_fields = ('id',)


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorNameSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('id',)

    def validate(self, data):
        if data.get('genre') == 'horror':
            raise serializers.ValidationError('Movie genre must not be horror')
        if data.get('year') < 1850:
            raise serializers.ValidationError('Movie year must be at least 1850')
        return data
