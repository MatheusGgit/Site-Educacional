# Generated by Django 4.0.4 on 2022-06-04 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Paginas', '0039_cursosfavorito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/img_Cursos'),
        ),
        migrations.CreateModel(
            name='AulasAssistida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assistido', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Paginas.usuarios')),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Paginas.video')),
            ],
        ),
    ]