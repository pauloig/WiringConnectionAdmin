# Generated by Django 4.0.6 on 2023-08-31 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0085_payrollaudit'),
    ]

    operations = [
        migrations.CreateModel(
            name='logInAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operationDetail', models.TextField(blank=True, max_length=1000, null=True)),
                ('operationType', models.CharField(blank=True, max_length=60, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_supervisor', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superAdmin', models.BooleanField(default=False)),
                ('accounts_payable', models.BooleanField(default=False)),
                ('createdBy', models.CharField(blank=True, max_length=60, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('updatedBy', models.CharField(blank=True, max_length=60, null=True)),
                ('EmployeeID', models.ForeignKey(db_column='EmployeeID', on_delete=django.db.models.deletion.CASCADE, to='workOrder.employee')),
                ('Location', models.ForeignKey(db_column='Location', on_delete=django.db.models.deletion.CASCADE, to='workOrder.locations')),
                ('Period', models.ForeignKey(db_column='Period', on_delete=django.db.models.deletion.CASCADE, to='workOrder.period')),
            ],
        ),
    ]