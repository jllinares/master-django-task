# Generated by Django 5.0.3 on 2024-04-25 01:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 25, 1, 25, 8, 49815, tzinfo=datetime.timezone.utc)),
        ),
    ]