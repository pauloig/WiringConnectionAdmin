# Generated by Django 4.0.6 on 2022-10-05 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0017_payroll_woid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='Status',
            field=models.CharField(blank=True, choices=[('1', 'Not Started'), ('2', 'Work in Progress'), ('3', 'Pending Docs'), ('4', 'Pending Revised WO'), ('5', 'Invoiced')], max_length=20, null=True),
        ),
    ]
