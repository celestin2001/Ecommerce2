# Generated by Django 4.1.2 on 2023-09-27 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionproduit', '0003_alter_commentaire_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='image',
            field=models.FileField(upload_to='media/media'),
        ),
    ]
