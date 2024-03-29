# Generated by Django 4.0.6 on 2023-01-21 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0039_internalpo_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internalpo',
            name='receipt',
            field=models.FileField(null=True, upload_to='po'),
        ),
        migrations.CreateModel(
            name='externalProduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceNumber', models.CharField(blank=True, max_length=60, null=True)),
                ('quantity', models.IntegerField()),
                ('total', models.FloatField(blank=True, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=60, null=True)),
                ('invoice', models.ImageField(null=True, upload_to='external_invoice')),
                ('itemID', models.ForeignKey(db_column='itemID', on_delete=django.db.models.deletion.CASCADE, to='workOrder.itemprice')),
                ('woID', models.ForeignKey(db_column='woID', on_delete=django.db.models.deletion.CASCADE, to='workOrder.workorder')),
            ],
        ),
    ]
