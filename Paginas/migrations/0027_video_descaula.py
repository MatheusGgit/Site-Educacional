# Generated by Django 4.0.4 on 2022-05-27 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paginas', '0026_remove_usuarios_teste_usuarios_usertheme'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='descAula',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
