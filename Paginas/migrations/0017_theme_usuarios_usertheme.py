# Generated by Django 4.0.4 on 2022-05-27 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Paginas', '0016_remove_usuarios_mostrar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='usuarios',
            name='userTheme',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Paginas.theme'),
        ),
    ]
