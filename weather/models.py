from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=200)
    user = models.ManyToManyField(User, related_name='cities', blank=True)
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
