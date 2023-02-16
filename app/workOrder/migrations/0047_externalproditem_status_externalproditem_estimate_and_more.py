# Generated by Django 4.0.6 on 2023-01-25 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0046_authorizedbilling_status_authorizedbilling_estimate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='externalproditem',
            name='Status',
            field=models.IntegerField(choices=[(1, 'Open'), (2, 'Estimated'), (3, 'Invoiced')], default=1),
        ),
        migrations.AddField(
            model_name='externalproditem',
            name='estimate',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='externalproditem',
            name='invoice',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]