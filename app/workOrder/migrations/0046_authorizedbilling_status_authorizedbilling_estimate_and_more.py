# Generated by Django 4.0.6 on 2023-01-25 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0045_authorizedbilling'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorizedbilling',
            name='Status',
            field=models.IntegerField(choices=[(1, 'Open'), (2, 'Estimated'), (3, 'Invoiced')], default=1),
        ),
        migrations.AddField(
            model_name='authorizedbilling',
            name='estimate',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='authorizedbilling',
            name='invoice',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dailyitem',
            name='Status',
            field=models.IntegerField(choices=[(1, 'Open'), (2, 'Estimated'), (3, 'Invoiced')], default=1),
        ),
        migrations.AddField(
            model_name='dailyitem',
            name='estimate',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dailyitem',
            name='invoice',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]