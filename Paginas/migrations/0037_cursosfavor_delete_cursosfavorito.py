# Generated by Django 4.0.4 on 2022-05-30 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paginas', '0036_cursosfavorito'),
    ]

    operations = [
        migrations.CreateModel(
            name='CursosFavor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.ManyToManyField(blank=True, to='Paginas.cursos')),
            ],
        ),
        migrations.DeleteModel(
            name='CursosFavorito',
        ),
    ]
