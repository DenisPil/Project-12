# Generated by Django 4.0.2 on 2022-03-24 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='is_admin',
        ),
        migrations.AlterField(
            model_name='staff',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]