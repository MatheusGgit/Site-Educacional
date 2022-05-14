# Generated by Django 4.0.4 on 2022-05-13 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paginas', '0011_cursos_categoriaid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursos',
            name='categoriaID',
        ),
        migrations.AlterField(
            model_name='cursos',
            name='usuarioID',
            field=models.ManyToManyField(blank=True, to='Paginas.usuarios'),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
