# Generated by Django 4.1.2 on 2023-10-11 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionproduit', '0015_commande_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='date_commande',
            field=models.DateField(auto_now=True),
        ),
    ]