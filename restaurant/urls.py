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
from restapp.views import RestaurantsList, MenuList, IndexView, ProfileUpdate, UserRedirectView, RestaurantIndex,\
    CustomerIndex, WelcomeView, CreateItemView, UserCreate, CustomerOrderView, RestaurantUpdate, CustomerUpdate, \
    RestaurantOrderView, ItemListView, CompOrderView, ItemUpdateView, RemoveOrderView, \
    BuildOrderView, AddToOrderView, SubmitOrderView

urlpatterns = [
    url(r'^restaurant/$', RestaurantsList.as_view(), name='restaurant_list'),
    url(r'^menu/(?P<user_id>\d+)/$', MenuList.as_view(), name='menu'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^user_redirect', UserRedirectView.as_view(), name='user_redirect'),
    url(r'^update_profile/(?P<pk>\d+)/$', login_required(ProfileUpdate.as_view()), name='update_profile'),
    url(r'^restaurant/(?P<pk>\d+)/$', RestaurantIndex.as_view(), name='restaurant_index'),
    url(r'^restaurant/order/(?P<pk>\d+)/$', RestaurantOrderView.as_view(), name='restaurant_order_view'),
    url(r'^restaurant/order/removed/(?P<order_id>\d+)/$', RemoveOrderView.as_view(), name='remove_order'),
    url(r'^restaurant/completed/(?P<pk>\d+)/$', CompOrderView.as_view(), name='comp_order_view'),
    url(r'^customer/(?P<pk>\d+)/$', CustomerIndex.as_view(), name='customer_index'),
    url(r'^customer/order/(?P<pk>\d+)/$', CustomerOrderView.as_view(), name='customer_order_view'),
    url(r'^welcome/', WelcomeView.as_view(), name='welcome'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^restaurant/create_item/$', CreateItemView.as_view(), name='create_item'),
    url(r'^create_user/', UserCreate.as_view(), name='create_user'),
    url(r'^update_restaurant/(?P<pk>\d+)/$', login_required(RestaurantUpdate.as_view()), name='restaurant_update'),
    url(r'^update_customer/(?P<pk>\d+)/$', login_required(CustomerUpdate.as_view()), name='customer_update'),
    url(r'^restaurant/menu_view/(?P<pk>\d+)/$', ItemListView.as_view(), name='menu_view'),
    url(r'^restaurant/update/(?P<pk>\d+)/$', ItemUpdateView.as_view(), name="item_update"),
    url(r'^restaurant/build_order/(?P<pk>\d+)/$', login_required(BuildOrderView.as_view()), name='build_order'),
    url(r'^add_to_order/(?P<item_id>\d+)/$', AddToOrderView.as_view(), name='add_to_order'),
    url(r'^submit_order/(?P<order_id>\d+)/$', SubmitOrderView.as_view(), name='submit_order')
]
