# Generated by Django 4.1.2 on 2023-09-27 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionproduit', '0002_commentaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='image',
            field=models.FileField(upload_to='%Y%m%d'),
        ),
    ]
