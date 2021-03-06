# Generated by Django 3.0.6 on 2020-06-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200620_2301'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='fooditem',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='fooditem',
            constraint=models.UniqueConstraint(fields=('name', 'restaurant_id'), name='unique_food_name'),
        ),
    ]
