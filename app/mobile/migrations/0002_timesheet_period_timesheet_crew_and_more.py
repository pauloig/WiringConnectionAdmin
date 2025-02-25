# Generated by Django 4.0.6 on 2024-10-25 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0096_alter_woadjustment_estimatenumber_and_more'),
        ('mobile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='Period',
            field=models.ForeignKey(blank=True, db_column='Period', null=True, on_delete=django.db.models.deletion.CASCADE, to='workOrder.period'),
        ),
        migrations.AddField(
            model_name='timesheet',
            name='crew',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='timesheet',
            name='tranferredBy',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='timesheet',
            name='transferred_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
