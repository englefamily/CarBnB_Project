# Generated by Django 4.1.5 on 2023-02-21 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_bnb_app', '0003_car_renters_alter_car_owner_alter_rent_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='plate_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='renters',
            field=models.ManyToManyField(blank=True, null=True, related_name='rented_cars', through='car_bnb_app.Rent', to='car_bnb_app.person'),
        ),
    ]
