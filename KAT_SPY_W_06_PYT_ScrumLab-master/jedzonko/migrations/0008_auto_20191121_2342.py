# Generated by Django 2.2.6 on 2019-11-21 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0007_auto_20191121_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]