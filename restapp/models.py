from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import ForeignKey, CharField, FloatField


class Item(models.Model):
    item_name = CharField(max_length=50)
    description = CharField(max_length=200)
    price = FloatField()
    owner = ForeignKey(User)


class Profile(models.Model):
    name = ForeignKey(User)
    address = CharField(max_length=200)
    cuisine = CharField(max_length=15)
    allergies = models.TextField()
    type = models.CharField(max_length=1)

    def __str__(self):
        return self.body


class Order(models.Model):
    user = ForeignKey(User)
    items = models.ManyToManyField(Item) # Should this be a get function?
    timestamp = models.DateTimeField(auto_now=True)
    fulfilled = models.BooleanField()
    comments = models.TextField()

