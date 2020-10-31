# Generated by Django 3.1.2 on 2020-10-31 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees_api', '0004_auto_20201031_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='type',
            field=models.CharField(choices=[('Inventory Manager', 'Inventory Manager'), ('Quality Check Person', 'Quality Check Person'), ('Sales Manager', 'Sales Manager'), ('IT Admin', 'It Admin')], default='Inventory Manager', max_length=120),
        ),
    ]
