# Generated by Django 4.0.4 on 2022-05-27 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Paginas', '0023_alter_usuarios_usertheme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='userTheme',
        ),
    ]
