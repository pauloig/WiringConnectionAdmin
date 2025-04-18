# Generated by Django 4.0.6 on 2024-10-25 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workOrder', '0096_alter_woadjustment_estimatenumber_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timesheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.IntegerField(blank=True, null=True)),
                ('start_lunch_time', models.IntegerField(blank=True, null=True)),
                ('end_lunch_time', models.IntegerField(blank=True, null=True)),
                ('end_time', models.IntegerField(blank=True, null=True)),
                ('total_hours', models.FloatField(blank=True, null=True)),
                ('regular_hours', models.FloatField(blank=True, null=True)),
                ('ot_hour', models.FloatField(blank=True, null=True)),
                ('double_time', models.FloatField(blank=True, null=True)),
                ('start_mileage', models.IntegerField(blank=True, null=True)),
                ('end_mileage', models.IntegerField(blank=True, null=True)),
                ('total_mileage', models.IntegerField(blank=True, null=True)),
                ('Status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Sent'), (3, 'Pending'), (4, 'Approved'), (5, 'Rejected')], default=1)),
                ('comments', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=60, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('updatedBy', models.CharField(blank=True, max_length=60, null=True)),
                ('EmployeeID', models.ForeignKey(db_column='EmployeeID', on_delete=django.db.models.deletion.CASCADE, to='workOrder.employee')),
                ('Location', models.ForeignKey(db_column='Location', on_delete=django.db.models.deletion.CASCADE, to='workOrder.locations')),
            ],
            options={
                'unique_together': {('EmployeeID', 'date')},
            },
        ),
    ]
