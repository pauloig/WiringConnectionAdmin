# Generated by Django 4.0.6 on 2025-02-04 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0005_dailymob_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailymob',
            name='crew_by_user',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
