# Generated by Django 4.0.2 on 2022-03-24 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contract', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateField(verbose_name='eventdate')),
                ('number_guests', models.IntegerField(blank=True, null=True)),
                ('event_status', models.CharField(choices=[('paiement en cours', 'Payment In Progress'), ('payé', 'Full Payment'), ('événement à venir', 'Future Event'), ('événement en cours', 'Current Event'), ('événement terminé', 'Ended Event')], max_length=32)),
                ('commentary', models.TextField(max_length=256)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('contract_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractevent', to='contract.contract')),
                ('support_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supportcontact', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
