# Generated by Django 4.0 on 2022-05-16 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dboyride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dusername', models.CharField(max_length=30)),
                ('Ddate', models.CharField(max_length=100, verbose_name='Date')),
                ('startride', models.DecimalField(decimal_places=2, max_digits=5)),
                ('endride', models.DecimalField(decimal_places=2, max_digits=5)),
                ('totalride', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'Dboyride',
            },
        ),
        migrations.CreateModel(
            name='Delivery_Boy_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DName', models.CharField(max_length=50)),
                ('DLast_Name', models.CharField(max_length=50)),
                ('Dusername', models.CharField(max_length=30)),
                ('Dgender', models.CharField(max_length=30)),
                ('Dage', models.CharField(max_length=15)),
                ('DPhone_Number', models.CharField(max_length=50)),
                ('DLocation', models.CharField(blank=True, max_length=50, null=True)),
                ('Demail', models.EmailField(max_length=254)),
                ('Dpassword', models.CharField(max_length=30)),
                ('group', models.CharField(blank=True, max_length=255, null=True)),
                ('order', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FixedForAll',
            fields=[
                ('CustomerID', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('Customer_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Address', models.TextField(blank=True, null=True)),
                ('Phone_No', models.CharField(blank=True, max_length=255, null=True)),
                ('Plan', models.TextField(blank=True, null=True)),
                ('Total_milk', models.CharField(blank=True, max_length=255, null=True)),
                ('Company_name', models.CharField(max_length=255)),
                ('Group', models.CharField(blank=True, max_length=255, null=True)),
                ('dboy', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('bottles', models.IntegerField(blank=True, null=True)),
                ('remaining_bottles', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerID', models.CharField(max_length=255)),
                ('Customer_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Address', models.CharField(blank=True, max_length=255, null=True)),
                ('Phone_No', models.CharField(blank=True, max_length=255, null=True)),
                ('Plan', models.CharField(blank=True, max_length=255, null=True)),
                ('Total_milk', models.CharField(blank=True, max_length=255, null=True)),
                ('Company_name', models.CharField(max_length=255)),
                ('DeliveryBoy', models.CharField(blank=True, max_length=100, verbose_name='DeliveryBoy')),
                ('Ddate', models.CharField(max_length=100, verbose_name='Date')),
                ('ogroup', models.CharField(max_length=255, verbose_name='Group Name')),
                ('status', models.CharField(max_length=100, verbose_name='Delivery Status')),
                ('bottles', models.IntegerField(blank=True, null=True)),
                ('remaining_bottles', models.IntegerField(blank=True, null=True)),
                ('cust_comment', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'OrderHistory',
            },
        ),
    ]
