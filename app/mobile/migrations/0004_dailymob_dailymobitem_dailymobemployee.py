# Generated by Django 4.0.6 on 2025-01-29 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0096_alter_woadjustment_estimatenumber_and_more'),
        ('mobile', '0003_alter_timesheet_crew'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyMob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crew', models.IntegerField()),
                ('day', models.DateField()),
                ('supervisor', models.CharField(blank=True, max_length=200, null=True)),
                ('own_vehicle', models.FloatField(blank=True, null=True)),
                ('total_pay', models.FloatField(blank=True, null=True)),
                ('split_paymet', models.BooleanField(default=False)),
                ('pdfDaily', models.FileField(null=True, upload_to='dailys')),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('Location', models.ForeignKey(db_column='Location', on_delete=django.db.models.deletion.CASCADE, to='workOrder.locations')),
                ('Period', models.ForeignKey(db_column='Period', on_delete=django.db.models.deletion.CASCADE, to='workOrder.period')),
                ('woID', models.ForeignKey(blank=True, db_column='woID', null=True, on_delete=django.db.models.deletion.CASCADE, to='workOrder.workorder')),
            ],
            options={
                'unique_together': {('Period', 'Location', 'day', 'crew')},
            },
        ),
        migrations.CreateModel(
            name='DailyMobItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('emp_payout', models.FloatField(blank=True, null=True)),
                ('estimate', models.CharField(blank=True, max_length=50, null=True)),
                ('invoice', models.CharField(blank=True, max_length=50, null=True)),
                ('Status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Sent'), (3, 'Pending'), (4, 'Approved'), (5, 'Rejected')], default=1)),
                ('isAuthorized', models.BooleanField(default=False)),
                ('authorized_date', models.DateTimeField(blank=True, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=60, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('updatedBy', models.CharField(blank=True, max_length=60, null=True)),
                ('DailyID', models.ForeignKey(db_column='DailyID', on_delete=django.db.models.deletion.CASCADE, to='mobile.dailymob')),
                ('autorizedID', models.ForeignKey(blank=True, db_column='autorizedID', null=True, on_delete=django.db.models.deletion.SET_NULL, to='workOrder.authorizedbilling')),
                ('itemID', models.ForeignKey(db_column='itemID', on_delete=django.db.models.deletion.CASCADE, to='workOrder.itemprice')),
            ],
            options={
                'unique_together': {('DailyID', 'itemID')},
            },
        ),
        migrations.CreateModel(
            name='DailyMobEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_to_pay', models.FloatField(blank=True, null=True)),
                ('on_call', models.FloatField(blank=True, null=True)),
                ('bonus', models.FloatField(blank=True, null=True)),
                ('start_time', models.IntegerField(blank=True, null=True)),
                ('start_lunch_time', models.IntegerField(blank=True, null=True)),
                ('end_lunch_time', models.IntegerField(blank=True, null=True)),
                ('end_time', models.IntegerField(blank=True, null=True)),
                ('total_hours', models.FloatField(blank=True, null=True)),
                ('regular_hours', models.FloatField(blank=True, null=True)),
                ('rt_pay', models.FloatField(blank=True, null=True)),
                ('ot_hour', models.FloatField(blank=True, null=True)),
                ('ot_pay', models.FloatField(blank=True, null=True)),
                ('double_time', models.FloatField(blank=True, null=True)),
                ('dt_pay', models.FloatField(blank=True, null=True)),
                ('payout', models.FloatField(blank=True, null=True)),
                ('emp_rate', models.FloatField(blank=True, null=True)),
                ('production', models.FloatField(blank=True, null=True)),
                ('billableHours', models.BooleanField(default=False)),
                ('estimate', models.CharField(blank=True, max_length=50, null=True)),
                ('invoice', models.CharField(blank=True, max_length=50, null=True)),
                ('Status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Sent'), (3, 'Pending'), (4, 'Approved'), (5, 'Rejected')], default=1)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('DailyID', models.ForeignKey(db_column='DailyID', on_delete=django.db.models.deletion.CASCADE, to='mobile.dailymob')),
                ('EmployeeID', models.ForeignKey(db_column='EmployeeID', on_delete=django.db.models.deletion.CASCADE, to='workOrder.employee')),
            ],
            options={
                'unique_together': {('DailyID', 'EmployeeID')},
            },
        ),
    ]
