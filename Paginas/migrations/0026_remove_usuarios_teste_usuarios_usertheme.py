# Generated by Django 4.0.4 on 2022-05-27 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Paginas', '0025_usuarios_teste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='teste',
        ),
        migrations.AddField(
            model_name='usuarios',
            name='userTheme',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Paginas.theme'),
        ),
    ]
