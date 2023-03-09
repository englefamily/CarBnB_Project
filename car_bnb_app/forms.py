from django import forms
from django.forms import ModelForm
from .models import Car, Person
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class CarForm(ModelForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = Car
        fields = "__all__"
        # exclude = ["car_year"]


class DatePicker(forms.TextInput):
    input_type = "date"


def myValidator(value):
    if value % 2 != 0:
        raise ValidationError(message="Even Numbers Only")


def stupidValidator(value):
    if value % 2 != 0:
        raise ValidationError(message="Stupid Error Happened")


class Search(forms.Form):
    car_type_str = forms.CharField(max_length=10, required=False)
    year_str = forms.IntegerField(max_value=2024, min_value=1950)
    email = forms.EmailField(required=False)
    terms_of_use = forms.BooleanField()
    car_type = forms.CharField(widget=forms.TextInput(attrs={"style": "background-color: blue"}))
    number = forms.IntegerField(validators=[myValidator, stupidValidator])
    story = forms.CharField(max_length=20000, required=False, widget=forms.Textarea(attrs={"rows": 5}),
                            validators=[RegexValidator("[a-z]", message="letters only")])
    gender = forms.ChoiceField(choices=[
        ("male", 'Male'),
        ("female", 'Female'),
        ("confused", 'Confused about how Nature works')
    ])
    cars = forms.ModelChoiceField(queryset=Car.objects.all())
    date = forms.DateField(widget=forms.SelectDateWidget(years=range(1950,2150)))
    date1 = forms.DateField(widget=DatePicker)
    file = forms.FileField(required=False)


class ContactForm(forms.Form):
    car = forms.ModelChoiceField(queryset=Car.objects.all())
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.TextInput()

class PersonCreationForm(forms.ModelForm):
    # class Meta:
    #     model = Person
    pass


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)