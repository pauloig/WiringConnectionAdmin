# Generated by Django 4.0.6 on 2023-04-03 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0072_billingaddress_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingaddress',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
