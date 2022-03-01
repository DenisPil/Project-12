# Generated by Django 4.0.2 on 2022-03-01 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_alter_customer_mobile_alter_customer_phone'),
        ('contract', '0002_rename_is_signed_contract_status_contract_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='client',
        ),
        migrations.AlterField(
            model_name='contract',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
    ]
