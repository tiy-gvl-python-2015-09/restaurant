from django.contrib.auth.models import User
from django.test import TestCase
from restapp.models import Profile


"""None of these tests pass yet.
    I can't figure out why yet. ~TK"""



class RestaurantTests(TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName='runTest')
        self.user_id = None


    def setUp(self):
        self.rest1 = User.objects.create(user_id="joesinn", usertype="restaurant")
        self.rest2 = User.objects.create(user_id="daisies", usertype="restaurant")
        self.rest3 = User.objects.create(user_id="chinaone", usertype="restaurant")

    def test_restaurant_exists_in_restaurant_list(self):
        Profile.objects.create(self.rest1)
        assert "joesinn" in self.ProfileManager.filter_for_restaurants()
