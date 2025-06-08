
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloApiView.as_view()),
    path('actors/', ActorsAPIView.as_view()),
    path('actors/<int:pk>/', ActorRetrieveUpdateDeleteAPIView.as_view()),
]
