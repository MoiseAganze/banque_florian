# Generated by Django 5.1.4 on 2024-12-15 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Utilisateur', '0002_emailconfirmer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmailConfirmer',
        ),
    ]
