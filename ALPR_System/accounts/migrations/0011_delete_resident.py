# Generated by Django 3.2.3 on 2021-08-12 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_customer_profile_picture'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Resident',
        ),
    ]
