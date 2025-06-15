from rest_framework import status, viewsets
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
import datetime


class ActorViewSet(ModelViewSet):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()


class SubscriptionAPIView(APIView):
    def get(self, request):
        subscriptions = Subscription.objects.all()
        serializer = SubjectSerializer(subscriptions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class SubscriptionRetrieveUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Subscription, pk=pk)

    def get(self, request, pk):
        subscription = self.get_object(pk)
        serializer = SubjectSerializer(subscription)
        return Response(serializer.data)

    def put(self, request, pk):
        subscription = self.get_object(pk)
        serializer = SubjectSerializer(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, pk):
        subscription = self.get_object(pk)
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MoviesAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieRetrieveUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Movie, pk=pk)

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == 'add_actor':
            return ActorSerializer
        return self.serializer_class

    @action(detail=True, methods=['GET'])
    def actors(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        actors = movie.actors.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'], url_path='add_actor')
    def add_actor(self, request, pk):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            actor = serializer.save()
            movie = get_object_or_404(Movie, pk=pk)
            movie.actors.add(actor)
            movie.save()
            response = {
                'success': True,
                'actor': ActorSerializer(actor).data,
                'movie': MovieSerializer(movie).data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
