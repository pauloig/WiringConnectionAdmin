# Generated by Django 4.0.6 on 2023-04-07 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0074_woestimate_description_woinvoice_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorizedbilling',
            name='transferBy',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='authorizedbilling',
            name='transferFrom',
            field=models.ForeignKey(blank=True, db_column='transferFrom', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transferFrom', to='workOrder.workorder'),
        ),
        migrations.AddField(
            model_name='authorizedbilling',
            name='transferTo',
            field=models.ForeignKey(blank=True, db_column='transferTo', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transferTo', to='workOrder.workorder'),
        ),
        migrations.AddField(
            model_name='authorizedbilling',
            name='transfer_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]