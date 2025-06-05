from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
import datetime


class HelloApiView(APIView):
    def get(self, request):
        return Response(
            {"message": "Hello World!",
             "current_time": datetime.datetime.now(),
            }
        )

    def post(self, request):
        return Response(
            "success"
        )


class ActorListApiView(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)