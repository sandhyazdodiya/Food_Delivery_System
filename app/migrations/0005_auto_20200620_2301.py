# Generated by Django 3.0.6 on 2020-06-20 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200620_2250'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='fooditem',
            name='unique_food_name',
        ),
        migrations.AlterUniqueTogether(
            name='fooditem',
            unique_together={('name', 'restaurant_id')},
        ),
    ]
