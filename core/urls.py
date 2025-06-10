
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloApiView.as_view()),
    path('actors/', ActorsAPIView.as_view()),
    path('actors/<int:pk>/', ActorRetrieveUpdateDeleteAPIView.as_view()),
    path('subscriptions/', SubscriptionAPIView.as_view()),
    path('subscriptions/<int:pk>/', SubscriptionRetrieveUpdateDeleteAPIView.as_view()),
    path('movies/', MoviesAPIView.as_view()),
    path('movies/<int:pk>/', MovieRetrieveUpdateDeleteAPIView.as_view()),

]
