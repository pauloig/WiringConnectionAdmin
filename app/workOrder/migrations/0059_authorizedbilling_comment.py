# Generated by Django 4.0.6 on 2023-02-17 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0058_woinvoice_is_partial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorizedbilling',
            name='comment',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
