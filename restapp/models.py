from django.contrib.auth.models import User
from django.db import models

# Create your models here.
import django.db.models
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProfileManager(models.Manager):
    """Untested!
    ProfileManager (and 'objects = ProfileManager' in 'class Profile' below)
    should make it easier to distinguish customers from restaurants"""

    def filter_restaurants(self):
        return self.all().filter(user_type="restaurant")

    def filter_customers(self):
        return self.all().filter(user_type="customer")


class Profile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    phone_num = models.CharField(max_length=25, blank=True)
    cuisine = models.IntegerField(choices=[(1, "American"), (2, "Italian"), (3, "Japanese"), (4, "Other")], null=True)
    allergies = models.TextField(blank=True)
    user_type = models.CharField(max_length=20, choices=[("restaurant", "Restaurant"), ("customer", "Customer")], null=True)

        # ties to ProfileManager, as per joel's twitter clone:
    objects = ProfileManager()

    def __str__(self):
        return self.user.username

    @property
    def customer_open_order(self):
        return Order.objects.filter(customer = self.user, submitted=False)


@receiver(post_save, sender=User)
def user_post_save(sender, **kwargs):
    instance = kwargs.get("instance")
    created = kwargs.get("created")
    if created:
        Profile.objects.create(user=instance)


class Item(models.Model):
    item_name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    owner = models.ForeignKey(User)
    display = models.BooleanField()

    def __str__(self):
        return self.item_name


class Order(models.Model):
    customer = models.ForeignKey(User, related_name='customer')
    restaurant = models.ForeignKey(User, related_name='restaurant')
    items = models.ManyToManyField(Item, through='ItemCounter')
    timestamp = models.DateTimeField(auto_now_add=True)
    fulfilled = models.BooleanField()
    comments = models.TextField(blank=True)
    submitted = models.BooleanField()


    @property
    def total_cost(self):
        item_costs = []
        for item in self.items.all():
            itemcounter = ItemCounter.objects.get(item=item, order=self)
            item_costs.append(itemcounter.item_cost)
        return sum(item_costs)


class ItemCounter(models.Model):
    item = models.ForeignKey(Item)
    order = models.ForeignKey(Order)
    count = models.IntegerField()

    @property
    def item_cost(self):
        return self.item.price * self.count