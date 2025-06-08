from rest_framework import status
from rest_framework.generics import ListAPIView, get_object_or_404
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


# class ActorListAPIView(APIView):
#     def get(self, request):
#         actors = Actor.objects.all()
#         serializer = ActorSerializer(actors, many=True)
#         response = {
#             "success": True,
#             "count": actors.count(),
#             "data": serializer.data
#         }
#         return Response(response, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = ActorSerializer(data=request.data)
#         if serializer.is_valid():
#             Actor.objects.create(
#                 name=serializer.data["name"],
#                 country=serializer.data["country"],
#                 gender=serializer.data["gender"],
#                 birthday=serializer.data["birthday"],
#             )
#             response = {
#                 "success": True,
#                 "data": serializer.data,
#             }
#             return Response(response, status=status.HTTP_201_CREATED)
#         response = {
#             "success": False,
#             "error": serializer.errors,
#         }
#         return Response(response, status=status.HTTP_400_BAD_REQUEST)

class ActorsAPIView(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ActorRetrieveUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Actor, pk=pk)


    def get(self, request, pk):
        actor = self.get_object(pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)


    def put(self, request, pk):
        actor = self.get_object(pk)
        serializer = ActorSerializer(actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        actor = self.get_object(pk)
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
