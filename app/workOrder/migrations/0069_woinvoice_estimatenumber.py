# Generated by Django 4.0.6 on 2023-03-20 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0068_alter_daily_total_pay'),
    ]

    operations = [
        migrations.AddField(
            model_name='woinvoice',
            name='estimateNumber',
            field=models.IntegerField(null=True),
        ),
    ]
