from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, View, CreateView, UpdateView, TemplateView
from restapp.models import Profile, Order, Item


class RestaurantsList(ListView):
    pass


class MenuList(ListView):
    pass


class IndexView(View):

    def get(self, request):
        if request.user.id == None:
            return HttpResponseRedirect(reverse("welcome"))
        elif request.user.profile.user_type == "restaurant":
            return HttpResponseRedirect(reverse("restaurant_index", kwargs={"pk": request.user.id}))
        elif request.user.profile.user_type == "customer":
            return HttpResponseRedirect(reverse("customer_index", kwargs={"pk": request.user.id}))


class WelcomeView(TemplateView):

    template_name = "welcome.html"


class UserCreate(CreateView):
    model = User
    success_url = "/accounts/login"
    form_class = UserCreationForm


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ["user_type"]
    success_url = "/"


class RestaurantUpdate(UpdateView):
    model = Profile
    fields = ["name", "address", "phone_number", "cuisine"]
    success_url = "/"


class CustomerUpdate(UpdateView):
    model = Profile
    fields = ["name", "address", "phone_number", "allergies"]
    pass


class UserRedirectView(View):

    def get(self, request):
        if request.user.profile.user_type == "restaurant":
            return HttpResponseRedirect(reverse("restaurant_index", kwargs={"pk": request.user.id}))
        elif request.user.profile.user_type == "customer":
            return HttpResponseRedirect(reverse("customer_index", kwargs={"pk": request.user.id}))
        else:
            return HttpResponseRedirect(reverse("update_profile", kwargs={"pk": request.user.id}))


class RestaurantIndex(TemplateView):

    template_name = "restaurant_index.html"

    def get_context_data(self, **kwargs):
        context = super(RestaurantIndex, self).get_context_data(**kwargs)
        context['object'] = User.objects.filter(id=kwargs["pk"])[0]
        return context


class CustomerIndex(TemplateView):

    template_name = "customer_index.html"

    def get_context_data(self, **kwargs):
        context = super(CustomerIndex, self).get_context_data(**kwargs)
        context['object'] = User.objects.filter(id=kwargs["pk"])[0]
        return context


class CustomerOrderView(ListView):
    model = Order

    def get_queryset(self):
        user_id = self.kwargs.get("pk")
        return self.model.objects.filter(user__id=user_id)


class CreateItemView(CreateView):
    model = Item
