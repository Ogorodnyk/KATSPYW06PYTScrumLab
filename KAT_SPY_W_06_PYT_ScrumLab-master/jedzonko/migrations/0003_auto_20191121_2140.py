# Generated by Django 2.2.6 on 2019-11-21 20:40

from django.db import migrations, models
import jedzonko.models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0002_auto_20191120_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeplan',
            name='meal_name',
            field=models.CharField(choices=[(jedzonko.models.MealNames('Breakfast'), 'Breakfast'), (jedzonko.models.MealNames('Lunch'), 'Lunch'), (jedzonko.models.MealNames('Dinner'), 'Dinner'), (jedzonko.models.MealNames('Tea'), 'Tea'), (jedzonko.models.MealNames('Supper'), 'Supper')], max_length=24),
        ),
    ]
