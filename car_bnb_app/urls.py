from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    # path("cars/", views.cars),
    # path("cars/create_car", views.create_car),
    path("", views.default),
    path('home', views.home, name="home"),
    path("index", views.serve_msg),
    path("search_car", views.search_car, name='search_car'),
    path("contact", views.ContactView.as_view(), name='contact'),
    path("add_car/<str:cid>", views.add_car, name='add_car'),
    path("edit_car/<int:cid>", views.edit_car, name='edit_car'),
    path("cars_list", views.serve_cars, name='cars_list'),
    path("car_list", views.CarsListView.as_view()),
    path("create_person", views.PersonCreationForm.as_view(), name="create_person"),
    path("update_person/<slug:pk>", views.PersonUpdateView.as_view(), name="update_person"), # "/<int:pk>" did not seem to work correctly
    # path('login', views.connect, name="login"),
    path('login', views.UserLoginView.as_view(), name="login"),
    # path('logout', views.LogoutView.as_view(), name="logout"),
    # path('logout', views.logout_user, name="logout"),
    path('signup', views.create_user, name="signup"),
]
