# Generated by Django 4.0.5 on 2022-07-05 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webkiosk', '0002_food_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='quantiy',
            new_name='quantity',
        ),
    ]
