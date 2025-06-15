from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.views import *

router = DefaultRouter()
router.register('actors', ActorViewSet)
router.register('movies', MovieViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subscriptions/', SubscriptionAPIView.as_view()),
    path('subscriptions/<int:pk>/', SubscriptionRetrieveUpdateDeleteAPIView.as_view()),
    path('', include(router.urls))

]
