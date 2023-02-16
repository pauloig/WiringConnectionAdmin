# Generated by Django 4.0.6 on 2023-01-26 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0051_internalpo_status_internalpo_estimate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='woInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceNumber', models.IntegerField()),
                ('total', models.FloatField(blank=True, null=True)),
                ('Status', models.IntegerField(choices=[(1, 'Open'), (2, 'Closed')], default=1)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=60, null=True)),
                ('woID', models.ForeignKey(db_column='woID', on_delete=django.db.models.deletion.CASCADE, to='workOrder.workorder')),
            ],
        ),
    ]