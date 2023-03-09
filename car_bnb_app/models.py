from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Person(models.Model):
    # user = models.ForeignKey(User, unique=True, on_delete=models.RESTRICT)
    user = models.OneToOneField(User, on_delete=models.RESTRICT, null=False)
    first_name = models.CharField(null=False, max_length=50)
    last_name = models.CharField(null=False, max_length=50)
    age = models.IntegerField(null=False)
    address = models.CharField(null=False, max_length=50)

    class Meta:
        db_table = 'person'

    def __str__(self):
        return f"person: {self.first_name} {self.last_name}"


class Car(models.Model):
    car_type = models.CharField(null=False, max_length=50)
    car_year = models.PositiveIntegerField(null=False)
    plate_number = models.IntegerField(null=True, blank=True)
    cost = models.IntegerField(null=False)
    mileage = models.PositiveIntegerField(null=False)
    owner = models.ForeignKey("Person", on_delete=models.RESTRICT, related_name="car_owner", null=True) # models.CASCADE
    renters = models.ManyToManyField("Person", through="Rent", blank=True, related_name='rented_cars')

    class Meta:
        db_table = 'car'

    def __str__(self):
        return f"car: {self.car_type}"


class Rent(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    car = models.ForeignKey("Car", on_delete=models.RESTRICT)
    client = models.ForeignKey("Person", on_delete=models.RESTRICT)

    class Meta:
        db_table = 'rent'

    def __str__(self):
        return f"rent: {self.start_date}"
