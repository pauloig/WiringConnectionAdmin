# Generated by Django 4.0.6 on 2023-04-11 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0077_internalpo_ponumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizedbilling',
            name='transferQty',
            field=models.IntegerField(default=0),
        ),
    ]
