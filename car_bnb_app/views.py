from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.views import View
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Person, Car, Rent
from .forms import Search, ContactForm, CarForm, PersonCreationForm, LoginForm
from django.db.transaction import atomic
from django.core.validators import RegexValidator


def default(request):
    # return HttpResponse(reverse("search_car"))
    # return redirect("http://127.0.0.1:8000/home")
    return HttpResponse("Hello World!!"
                        " Straight-up Boring Page served by return HttpResponse in the 'default' function.")


def home(req):
    if req.user.is_authenticated:
        return HttpResponse(f"welcome {req.user}")
    else:
        return HttpResponse(f"welcome anonymous user")


def serve_msg(req):
    car = Car.objects.first()
    return render(request=req, template_name="car_bnb_app/index.html", context={"msg": car.car_type})


def search_car(req):
    if req.method == "GET":
        return render(request=req, template_name="car_bnb_app/search_car.html", context={'form': Search})
        # you can also set an initial value in the filed
        # return render(request=req, template_name="car_bnb_app/search_car.html",
        #           context={'form': Search(initial={"car_type_str": "example_str"})})

    elif req.method == 'POST':
        # search_str = req.POST['search_str'][0]
        # cars = Car.objects.filter(car_type__contains=search_str)
        # return render(request=req, template_name="car_bnb_app/cars_list.html", context={"cars": cars})

        file = req.FILES['File']
        new_file_path = str(settings.BASE_DIR) + rf"\car_bnb_app\uploaded_files\{file.name}"
        with open(new_file_path, "wb") as fh:
            for chunk in file.chunks():
                fh.write(chunk)
            return HttpResponse("File uploaded successfully")

    return HttpResponse("Not Implemented Yet")


# def search_car(req):
#     if req.method == "GET":
#         return render(request=req, template_name="car_bnb_app/search_car.html")
#
#     elif req.method == 'POST':
#         search_str = req.POST['search_str'][0]
#         cars = Car.objects.filter(car_type__contains=search_str)
#         return render(request=req, template_name="car_bnb_app/cars_list.html", context={"cars": cars})
#         # return render(request=req, template_name="car_bnb_app/index.html", context={"msg": str(cars)})
#         # return HttpResponse("Not Implemented Yet")


class ContactView(View):
    def get(self, request):
        # cars = Car.objects.all()
        # form = ContactForm(cars=cars)
        return render(request=request, template_name='car_bnb_app/contact.html', context={'form': ContactForm})

    def post(self, request):
        cars = Car.objects.all()
        form = ContactForm(request.POST, cars=cars)
        file = request.FILES['File']
        new_file_path = str(settings.BASE_DIR)+rf"\car_bnb_app\uploaded_files\{file.name}"
        with open(new_file_path, "wb") as fh:
            for chunk in file.chunks():
                fh.write(chunk)
            return HttpResponse("File uploaded successfully")
        # if form.is_valid():
        #     name = form.cleaned_data.get('name')
        #     email = form.cleaned_data.get('email')
        #     car = form.cleaned_data.get('car')
        #     message = form.cleaned_data.get('message')
        #     # Your code here to do something with the contact information
        #     return redirect('car_bnb_app/index')
        # return render(request, 'car_bnb_app/contact.html', {'form': form})


        # return HttpResponse('post')

class CarsListView(ListView):
    model = Car
    # template_name = "car_bnb_app/genericListView.html"
    template_name = "genericListView.html"
    context_object_name = "my_car_list"
    # queryset = Car.objects.filter(car_type__contains="t") # to filter
    queryset = Car.objects.all()  # to show all


class PersonCreationForm(CreateView):
    model = Person
    fields = "__all__"
    success_url = "/admin"


class PersonUpdateView(UpdateView):
    model = Person
    template_name = "car_bnb_app/person_update.html"
    fields = "__all__"
    success_url = "/admin"


def add_car(req):
    if req.method == 'GET':
        return render(request=req, template_name='car_bnb_app/add_car.html',
                      context={"form": CarForm()})
    elif req.method == 'POST':
        form = CarForm(data=req.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Car Added")
        else:
            return render(request=req, template_name='car_bnb_app/add_car.html', context={"form": form})


def edit_car(req, cid):
    if req.method == 'GET':
        try:
            car = Car.objects.get(pk=cid)
            form = CarForm(instance=car)
            return render(request=req, template_name="car_bnb_app/edit_car.html",
                          context={"form": form, "cid": cid})
        except Exception as e:
            return HttpResponse(f"Some error: {e}", status=500)
    elif req.method == 'POST':
        try:
            car = Car.objects.get(pk=cid)
            form = CarForm(instance=car, data=req.POST)

            if form.is_valid():
                form.save()
                return HttpResponse("Car Edited")
            else:
                return render(request=req, template_name="car_bnb_app/edit_car.html",
                              context={"form": form, "cid": cid})
        except Exception as e:
            return HttpResponse(f"Some error: {e}", status=500)


@require_http_methods(['GET'])
def serve_cars(req):
    cars = Car.objects.all()
    return render(request=req, template_name="car_bnb_app/cars_list.html",
                  context={"cars": cars})

def create_user(req):
    if req.method.lower() == "get":
        # return render(request=req, template_name="car_bnb_app/login.html",
        #               context={"form": LoginForm(), 'action': 'signup'})
        return render(request=req, template_name="car_bnb_app/login.html",
                      context={"form": UserCreationForm(), 'action': 'signup'})
    elif req.method.lower() == "post":
        # un = req.POST.get("username")
        # pw = req.POST.get("password")
        form = UserCreationForm(data=req.POST)
        # user = User.objects.create_user(username=un, password=pw)
        # login(request=req, user=user)
        if form.is_valid():
            form.save()
            login(request=req, user=form.instance)
            return redirect("home")
        else:
            return render(request=req, template_name="car_bnb_app/signup.html",
                          context={"form": form})


def connect(req):
    if req.method == "GET":
        return render(request=req, template_name="registrations/login.html",
                      context={"form": LoginForm(),
                               'action': 'login'})

    elif req.method == "POST":
        un = req.POST.get("username")
        pw = req.POST.get("password")

        user = authenticate(req, username=un, password=pw)

        if user is None:
            return HttpResponse(f"wrong user info")
        else:
            login(request=req, user=user)
            return HttpResponse(f"welcome {user.username}")

# Create your views here.
# @atomic # this or the one below
# def cars(request):
#     with atomic():
#         Car.objects.create(car_type=car_type, car_year=car_year, cost=cost, mileage=mileage, owner_id=owner_id) # just examples
#         Car.objects.create(car_type="dftbsbs2", owner_id=3)
#         Car.objects.create(car_type="dftbsbs3", owner_id=19)
#
#     return HttpResponse
#
#
# def create_car(request):
#     if request.method == 'POST':
#         car_type = request.POST.get('car_type')
#         car_year = request.POST.get('car_year')
#         cost = request.POST.get('cost')
#         mileage = request.POST.get('mileage')
#         owner_id = request.POST.get('owner_id')
#
#         Car.objects.create(
#             car_type=car_type,
#             car_year=car_year,
#             cost=cost,
#             mileage=mileage,
#             owner_id=owner_id
#         )
#         return HttpResponse('Car successfully created!')
#     else:
#         return render(request, 'create_car.html')
class UserLoginView(LoginView):
    redirect_authenticated_user = True
    def get_success_url(self):
        return redirect('/home')