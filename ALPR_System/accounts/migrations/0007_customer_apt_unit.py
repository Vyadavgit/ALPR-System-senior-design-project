# Generated by Django 3.2.3 on 2021-08-12 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_vehicle_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='apt_unit',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
