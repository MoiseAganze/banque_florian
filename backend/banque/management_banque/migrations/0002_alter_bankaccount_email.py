# Generated by Django 5.1.4 on 2024-12-21 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_banque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
