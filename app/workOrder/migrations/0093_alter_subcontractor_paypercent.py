# Generated by Django 4.0.6 on 2024-03-27 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0092_subcontractor_pay70percent_subcontractor_paypercent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcontractor',
            name='payPercent',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]