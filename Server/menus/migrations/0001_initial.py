# Generated by Django 3.2.9 on 2022-03-25 02:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commercialFood', models.CharField(max_length=10)),
                ('foodName', models.CharField(max_length=100)),
                ('foodCategory', models.CharField(max_length=100)),
                ('foodDetailCategory', models.CharField(max_length=100)),
                ('servingSize', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('foodKcal', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('sugar', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('carbohydrate', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('protein', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('fat', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cholesterol', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('fattyAcid', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('mealTime', models.IntegerField(default=0)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MenuToFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('foodId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.food')),
                ('menuId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.menu')),
            ],
        ),
    ]
