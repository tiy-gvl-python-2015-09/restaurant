from django.db import models

# Create your models here.
from django.db.models import ForeignKey, CharField, FloatField


class Item(models.Model):
    item_name = CharField(max_length=50)
    description = CharField(max_length=200)
    price = FloatField()
    owner = ForeignKey(Restaurant)


class Restaurant(models.Model):
    address = CharField(max_length=200)
    cuisine = CharField(max_length=15)

    def __str__(self):
        return self.body


class Order(models.Model):
    customer = ForeignKey(Customer)     # "Customer" doesn't exist yet
    restaurant = ForeignKey(Restaurant)
    items = models.ManyToManyField(Item) # Should this be a get function?
    timestamp = models.DateTimeField(autonow=True)
    fulfilled = models.BooleanField()
    comments = CharField(max_length=300)

