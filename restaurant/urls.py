"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from restapp.views import RestaurantsList, MenuList, IndexView, ProfileUpdate, UserRedirectView, RestaurantIndex, \
    CustomerIndex, WelcomeView

urlpatterns = [
    url(r'^restaurant', RestaurantsList.as_view(), name='restaurant_list'),
    url(r'^menu/(?P<user_id>\d+)/$', MenuList.as_view(), name='menu'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^user_redirect', UserRedirectView.as_view(), name='user_redirect'),
    url(r'^update_profile/(?P<pk>\d+)/$', login_required(ProfileUpdate.as_view()), name='update_profile'),
    url(r'^restaurant/(?P<pk>\d+)/$', RestaurantIndex.as_view(), name='restaurant_index'),
    url(r'^customer/(?P<pk>\d+)/$', CustomerIndex.as_view(), name='customer_index'),
    url(r'^welcome/', WelcomeView.as_view(), name='welcome'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
