# Generated by Django 5.0.4 on 2024-04-17 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователя', 'verbose_name_plural': 'Пользователей'},
        ),
    ]