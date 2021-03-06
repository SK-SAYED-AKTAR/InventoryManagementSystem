# Generated by Django 3.0.5 on 2021-06-01 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20210601_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_purchase',
            name='cgst',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='add_purchase',
            name='igst',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='add_purchase',
            name='invoiceDate',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 6, 1, 8, 26, 17, 650000)),
        ),
        migrations.AlterField(
            model_name='add_purchase',
            name='invoiceValue',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='add_purchase',
            name='paymentId',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='add_purchase',
            name='qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='add_purchase',
            name='sgst',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='add_purchase',
            name='taxableValue',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='add_purchase',
            name='total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='add_purchase',
            name='totalGst',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='addproduct',
            name='date',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 6, 1, 8, 26, 17, 647997)),
        ),
        migrations.AlterField(
            model_name='saleproduct',
            name='invoiceDate',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 6, 1, 8, 26, 17, 648999)),
        ),
    ]
