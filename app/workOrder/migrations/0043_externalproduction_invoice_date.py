# Generated by Django 4.0.6 on 2023-01-21 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0042_rename_total_externalproduction_total_invoice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='externalproduction',
            name='invoice_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]