# Generated by Django 3.0.6 on 2020-12-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20201024_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]