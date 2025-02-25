# Generated by Django 4.0.6 on 2025-02-07 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0007_dailymob_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailymob',
            name='approved_by',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='dailymob',
            name='approved_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dailymob',
            name='comments',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='dailymob',
            name='rejected_by',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='dailymob',
            name='rejected_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dailymob',
            name='send_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
