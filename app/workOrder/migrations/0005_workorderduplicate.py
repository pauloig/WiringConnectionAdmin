# Generated by Django 4.0.6 on 2022-08-18 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0004_alter_workorder_po_alter_workorder_poamount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='workOrderDuplicate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prismID', models.CharField(blank=True, max_length=200, null=True)),
                ('workOrderId', models.CharField(blank=True, max_length=200, null=True)),
                ('PO', models.CharField(blank=True, max_length=200, null=True)),
                ('POAmount', models.CharField(blank=True, max_length=200, null=True)),
                ('ConstType', models.CharField(blank=True, max_length=200, null=True)),
                ('ConstCoordinator', models.CharField(blank=True, max_length=200, null=True)),
                ('WorkOrderDate', models.CharField(blank=True, max_length=200, null=True)),
                ('EstCompletion', models.CharField(blank=True, max_length=200, null=True)),
                ('IssuedBy', models.CharField(blank=True, max_length=200, null=True)),
                ('JobName', models.CharField(blank=True, max_length=200, null=True)),
                ('JobAddress', models.CharField(blank=True, max_length=200, null=True)),
                ('SiteContactName', models.CharField(blank=True, max_length=200, null=True)),
                ('SitePhoneNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('Comments', models.CharField(blank=True, max_length=200, null=True)),
                ('Status', models.CharField(blank=True, max_length=200, null=True)),
                ('CloseDate', models.CharField(blank=True, max_length=200, null=True)),
                ('WCSup', models.CharField(blank=True, max_length=200, null=True)),
                ('UploadDate', models.CharField(blank=True, max_length=200, null=True)),
                ('UserName', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
