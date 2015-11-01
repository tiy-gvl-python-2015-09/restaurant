from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


# Create your views here.
from django.views.generic import ListView, View, CreateView, UpdateView, TemplateView
from restapp.models import Profile, Order, Item, ProfileManager, ItemCounter


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
                return HttpResponseRedirect(reverse("restaurant_order_view", kwargs={"pk": request.user.id}))
        elif request.user.profile.user_type == "customer":
            if request.user.profile.name == '':
                return HttpResponseRedirect(reverse("customer_update", kwargs={"pk": request.user.id}))
            else:
                return HttpResponseRedirect(reverse("restaurant_list",))
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
    fields = ['item_name', 'description', 'price', 'display']
    success_url = '/restaurant/menu_view/'

    def form_valid(self, form):
        model = form.save(commit=False)
        model.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('menu_view',args=(self.object.owner.id,))

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


class UnDisplayedItemListView(ListView):
    model = Item
    template_name = 'restapp/undisp_list.html'

    def get_queryset(self):
        user_id = self.kwargs.get("pk")
        return self.model.objects.filter(owner__id=user_id)


class ItemUpdateView(UpdateView):
    model = Item
    fields = ['item_name', 'description', 'price']
    
    def get_success_url(self):
        return reverse('menu_view',args=(self.object.owner.id,))


class RemoveOrderView(View):

    def post(self, request, order_id):
        order = Order.objects.get(id=order_id)
        order.fulfilled = True
        order.save()
        return HttpResponseRedirect(reverse('restaurant_order_view', kwargs={'pk': request.user.id}))

    def get_queryset(self):
        user_id = self.kwargs.get("pk")
        return self.model.objects.filter(restaurant__id=user_id)


class BuildOrderView(ListView):
    model = Item
    template_name = 'restapp/build_order_list.html'

    def get_queryset(self):
        user_id = self.kwargs.get("pk")
        return self.model.objects.filter(owner__id=user_id)


class AddToOrderView(View):

    def post(self, request, item_id):
        item = Item.objects.get(id=item_id)
        current_order = Order.objects.filter(customer=request.user, restaurant=item.owner, submitted=False)
        if not current_order:
            new_order = Order.objects.create(customer=request.user, restaurant=item.owner, submitted=False, fulfilled=False)
            ItemCounter.objects.create(item=item, order=new_order, count=1)
        elif len(current_order) == 1:
            order = current_order[0]
            itemcounter = ItemCounter.objects.filter(item=item, order=order)
            if not itemcounter:
                ItemCounter.objects.create(item=item, order=order, count=1)
            else:
                itemcounter = itemcounter[0]
                itemcounter.count += 1
                itemcounter.save()
        else:
            pass #direct to special page that shows they have more than 1 open order
        return HttpResponseRedirect(reverse("build_order", kwargs={"pk": item.owner.id}))


class DeleteFromOrderView(View):

    def post(self, request, item_id):
        item = Item.objects.get(id=item_id)
        current_order = Order.objects.filter(customer=request.user, restaurant=item.owner, submitted=False)
        order = current_order[0]
        itemcounter = ItemCounter.objects.get(item=item, order=order)
        if itemcounter.count > 1:
            itemcounter.count -= 1
            itemcounter.save()
        else:
            itemcounter.delete()
        return HttpResponseRedirect(reverse("build_order", kwargs={"pk": item.owner.id}))


class SubmitOrderView(View):

    def post(self, request, order_id):
        order = Order.objects.get(id=order_id)
        order.submitted = not order.submitted
        order.save()
        return HttpResponseRedirect(reverse("customer_order_view", kwargs={"pk": request.user.id}))


class CancelOrderView(View):

    def post(self,request, order_id):
        order = Order.objects.get(id=order_id)
        order.delete()
        return HttpResponseRedirect(reverse("customer_order_view", kwargs={"pk": request.user.id}))

class DisplayItemView(View):

    def post(self, request, item_id):
        item = Item.objects.get(id=item_id)
        item.display = not item.display
        item.save()
        return HttpResponseRedirect(reverse("undisp_menu_view", kwargs={"pk": request.user.id}))

class UnDisplayItemView(View):

    def post(self, request, item_id):
        item = Item.objects.get(id=item_id)
        item.display = not item.display
        item.save()
        return HttpResponseRedirect(reverse("menu_view", kwargs={"pk": request.user.id}))
