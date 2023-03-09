import  os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carbnb_project.settings")
import django
django.setup()
from car_bnb_app.models import Car, Person
from django.contrib.auth.models import User


# print(User.objects.all())
#
# u = User.objects.create_user(username="shimi", password="123")

# car = Car.objects.first()
# print(car.renters.all()) # car.owner.first_name
#
# p = car.renters.first()
# print(p.rented_cars.all())
#
# p = car.owner
# # print(car.owner)
# print(p.car_owner.all())

print(User.objects.all())

# u = User.objects.create_user(username="Yossi", email=None, password="123")
# print(u)

# u = User.objects.create_user(username="Bob", email=None, password="12345")
# print(u)


persons = Person.objects.all()

for i, p in enumerate(persons):
    if not p.user:
        user = User.objects.get(username=f"{p.first_name}_{str(i)}")
        user.delete()

        user = User.objects.create_user(username=f"{p.first_name}_{str(i)}", password="123")
        p.user = user
        p.save()
