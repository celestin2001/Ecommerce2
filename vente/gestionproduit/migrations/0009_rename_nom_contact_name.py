# Generated by Django 4.1.2 on 2023-09-28 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionproduit', '0008_alter_contact_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='nom',
            new_name='name',
        ),
    ]