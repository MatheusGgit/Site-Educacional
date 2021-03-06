# Generated by Django 4.0.4 on 2022-05-13 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Paginas', '0009_alter_cursos_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoriaCurso', models.CharField(max_length=55)),
            ],
        ),
        migrations.RemoveField(
            model_name='cursos',
            name='video',
        ),
        migrations.AddField(
            model_name='cursos',
            name='usuarioID',
            field=models.ManyToManyField(to='Paginas.usuarios'),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeAula', models.CharField(max_length=255)),
                ('video', models.FileField(upload_to='videos/%Y')),
                ('cursoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Paginas.cursos')),
            ],
        ),
    ]
