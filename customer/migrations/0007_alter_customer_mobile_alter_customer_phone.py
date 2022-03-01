# Generated by Django 4.0.2 on 2022-03-01 15:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_customer_mobile_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(max_length=32, validators=[django.core.validators.RegexValidator('^((\\+)33|0|0033)[1-9](\\d{2}){4}$')], verbose_name='mobile'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=32, null=True, validators=[django.core.validators.RegexValidator('^((\\+)33|0|0033)[1-9](\\d{2}){4}$')], verbose_name='phone'),
        ),
    ]