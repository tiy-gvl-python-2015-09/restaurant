from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

# Create your views here.
from django.views.generic import ListView, View, CreateView, UpdateView, TemplateView
from restapp.models import Profile, Order, Item, ProfileManager


class RestaurantsList(ListView):
    model = Profile
    template_name = "customer_index.html"


class MenuList(ListView):
    pass


class IndexView(View):

    def get(self, request):
        if request.user.id == None:
            return HttpResponseRedirect(reverse("welcome"))
        else:
            return HttpResponseRedirect(reverse("user_redirect"))


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
    fields = ["name", "address", "phone_num", "cuisine"]
    success_url = "/"


class CustomerUpdate(UpdateView):
    model = Profile
    fields = ["name", "address", "phone_num", "allergies"]
    success_url = '/'


class UserRedirectView(View):

    def get(self, request):
        if request.user.profile.user_type == "restaurant":
            if request.user.profile.name == '':
                return HttpResponseRedirect(reverse("restaurant_update", kwargs={"pk": request.user.id}))
            else:
                return HttpResponseRedirect(reverse("restaurant_index", kwargs={"pk": request.user.id}))
        elif request.user.profile.user_type == "customer":
            if request.user.profile.name == '':
                return HttpResponseRedirect(reverse("customer_update", kwargs={"pk": request.user.id}))
            else:
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
        return self.model.objects.filter(customer__id=user_id)


class CreateItemView(CreateView):
    model = Item
    fields = ['item_name', 'description', 'price']
    success_url = '/'

    def form_valid(self, form):
        model = form.save(commit=False)
        model.owner = self.request.user
        return super().form_valid(form)


class RestaurantOrderView(ListView):
    model = Order
    template_name = 'restapp/rest_order_list.html'

    def get_queryset(self):
        user_id = self.kwargs.get("pk")
        return self.model.objects.filter(restaurant__id=user_id)


class CompOrderView(ListView):
    model = Order
    template_name = 'restapp/comp_order_list.html'

    def get_queryset(self):
        user_id = self.kwargs.get("pk")
        return self.model.objects.filter(restaurant__id=user_id)

class ItemListView(ListView):
    model = Item

    def get_queryset(self):
        user_id = self.kwargs.get("pk")
        return self.model.objects.filter(owner__id=user_id)


class ItemUpdateView(UpdateView):
    model = Item
    fields = ['item_name', 'description', 'price']
    success_url = '/'


class RemoveOrderView(ListView):
    template_name = 'restapp/rest_order_list.html'

    def change_status(self, request, resturant_id):
        order = Order.objects.get(id=resturant_id)
        order.fulfilled = not order.fulfilled
        order.save()
        return HttpResponseRedirect('restaurant_order_view')
