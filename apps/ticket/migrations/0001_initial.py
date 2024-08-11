# Generated by Django 5.0.6 on 2024-08-03 14:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('ft_from', models.CharField(choices=[('Cuba', 'Cuba'), ('New York', 'New York'), ('Lisbon', 'Lisbon')], max_length=150, verbose_name='De')),
                ('ft_to', models.CharField(choices=[('Chicago', 'Chicago'), ('Madrid', 'Madrid'), ('Paris', 'París')], max_length=150, verbose_name='Para')),
                ('ft_date', models.DateField(verbose_name='Fecha')),
                ('ft_duration', models.IntegerField(choices=[('1', '1 Día'), ('3', '3 Días'), ('2', '2 Días')], verbose_name='Duración')),
                ('ft_adults', models.IntegerField(default=2, verbose_name='Adultos')),
                ('ft_children', models.IntegerField(default=0, verbose_name='Niños')),
                ('ft_check', models.BooleanField(default=False, verbose_name='Aprobada')),
                ('ft_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
            },
        ),
    ]
