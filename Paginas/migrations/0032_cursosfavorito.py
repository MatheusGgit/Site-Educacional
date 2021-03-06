# Generated by Django 4.0.4 on 2022-05-30 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Paginas', '0031_delete_cursosfavorito'),
    ]

    operations = [
        migrations.CreateModel(
            name='CursosFavorito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Paginas.cursos')),
                ('user_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Paginas.usuarios')),
            ],
        ),
    ]
