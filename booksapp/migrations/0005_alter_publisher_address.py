# Generated by Django 4.2.13 on 2024-06-26 07:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0004_alter_publisher_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='address',
            field=models.TextField(blank=True, default=datetime.datetime(2024, 6, 26, 7, 14, 24, 838142), null=True),
        ),
    ]