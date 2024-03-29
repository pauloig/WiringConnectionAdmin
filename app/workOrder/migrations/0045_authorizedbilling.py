# Generated by Django 4.0.6 on 2023-01-23 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0044_internalpo_nonbillable'),
    ]

    operations = [
        migrations.CreateModel(
            name='authorizedBilling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total', models.FloatField(blank=True, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=60, null=True)),
                ('itemID', models.ForeignKey(db_column='itemID', on_delete=django.db.models.deletion.CASCADE, to='workOrder.itemprice')),
                ('woID', models.ForeignKey(db_column='woID', on_delete=django.db.models.deletion.CASCADE, to='workOrder.workorder')),
            ],
        ),
    ]
