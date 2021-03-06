# Generated by Django 3.0.5 on 2021-06-01 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memberId', models.IntegerField(default=0, max_length=250)),
                ('memberPhoto', models.ImageField(blank=True, default=None, null=True, upload_to='MemberPhoto/')),
                ('memberName', models.CharField(default='N/A', max_length=250)),
                ('gurdianName', models.CharField(default='N/A', max_length=250)),
                ('phoneNo', models.IntegerField(default=0, max_length=10)),
                ('gender', models.CharField(default='N/A', max_length=6)),
                ('category', models.CharField(default='N/A', max_length=60)),
                ('landHolding', models.CharField(default='N/A', max_length=50)),
                ('memberType', models.CharField(default='N/A', max_length=50)),
                ('familyMember', models.CharField(default='N/A', max_length=90)),
                ('block', models.CharField(default='N/A', max_length=150)),
                ('village', models.CharField(default='N/A', max_length=250)),
                ('district', models.CharField(default='N/A', max_length=150)),
                ('state', models.CharField(default='N/A', max_length=150)),
                ('cropName', models.CharField(default='N/A', max_length=150)),
                ('irrigationSource', models.CharField(default='N/A', max_length=150)),
                ('kccLimit', models.CharField(default='N/A', max_length=150)),
                ('bankName', models.CharField(default='N/A', max_length=250)),
                ('ifscCode', models.CharField(default='N/A', max_length=250)),
                ('aadharNo', models.CharField(default='N/A', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='add_Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceDate', models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 6, 1, 8, 24, 28, 224730))),
                ('category', models.CharField(default='N/A', max_length=80)),
                ('productName', models.CharField(default='N/A', max_length=200)),
                ('invoiceNumber', models.IntegerField(default=0)),
                ('unit', models.CharField(default='N/A', max_length=50)),
                ('qty', models.IntegerField(default=0, max_length=30)),
                ('supplierName', models.CharField(default='N/A', max_length=150)),
                ('taxableValue', models.FloatField(default=0, max_length=30)),
                ('cgst', models.FloatField(default=0, max_length=30)),
                ('sgst', models.FloatField(default=0, max_length=30)),
                ('igst', models.FloatField(default=0, max_length=30)),
                ('totalGst', models.FloatField(default=0, max_length=30)),
                ('total', models.FloatField(default=0, max_length=30)),
                ('invoiceValue', models.IntegerField(default=0, max_length=50)),
                ('paymentMethod', models.CharField(default='N/A', max_length=350)),
                ('paymentId', models.IntegerField(default=0, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='addProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 6, 1, 8, 24, 28, 223729))),
                ('productName', models.CharField(default='N/A', max_length=200)),
                ('unit', models.CharField(default='N/A', max_length=10)),
                ('stock', models.FloatField(default=0)),
                ('rate', models.FloatField(default=0)),
                ('particulars', models.CharField(default='N/A', max_length=350)),
                ('openBal', models.FloatField(default=0)),
                ('clsBal', models.FloatField(default=0)),
                ('curBal', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='saleProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceDate', models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 6, 1, 8, 24, 28, 224730))),
                ('productName', models.CharField(default='N/A', max_length=200)),
                ('invoiceNumber', models.FloatField(default=0)),
                ('customerName', models.CharField(default='N/A', max_length=200)),
                ('customerGstin', models.FloatField(default=0, max_length=30)),
                ('qty', models.FloatField(default=0, max_length=30)),
                ('taxableValue', models.FloatField(default=0, max_length=30)),
                ('cgst', models.FloatField(default=0, max_length=30)),
                ('sgst', models.FloatField(default=0, max_length=30)),
                ('igst', models.FloatField(default=0, max_length=30)),
                ('totalGst', models.FloatField(default=0, max_length=30)),
                ('total', models.FloatField(default=0, max_length=30)),
                ('discount', models.FloatField(default=0, max_length=30)),
                ('due', models.FloatField(default=0, max_length=30)),
                ('paymentMethod', models.CharField(default='N/A', max_length=350)),
                ('invoiceValue', models.FloatField(default=0, max_length=30)),
            ],
        ),
    ]
