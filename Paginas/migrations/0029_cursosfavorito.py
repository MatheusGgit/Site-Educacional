# Generated by Django 4.0.4 on 2022-05-30 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Paginas', '0028_remove_cursos_horas'),
    ]

    operations = [
        migrations.CreateModel(
            name='CursosFavorito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Paginas.cursos')),
            ],
        ),
    ]