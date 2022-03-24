# Generated by Django 4.0.2 on 2022-03-24 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_remove_staff_is_admin_alter_staff_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]