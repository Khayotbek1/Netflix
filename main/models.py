from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

class GENDER(models.TextChoices):
    MALE = 'Male', 'Male'
    FEMALE = 'Female', 'Female'

class Actor(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, choices=GENDER.choices)
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, blank=True, null=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.name


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie.name} by {self.user.username}: {self.comment}'

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0)])
    duration = models.DurationField()

    def __str__(self):
        return self.name