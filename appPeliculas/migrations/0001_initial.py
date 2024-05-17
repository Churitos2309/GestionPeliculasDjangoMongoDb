# Generated by Django 4.1.13 on 2024-05-08 13:31

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(
                    auto_created=True, primary_key=True, serialize=False)),
                ('genNombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(
                    auto_created=True, primary_key=True, serialize=False)),
                ('pelCodigo', models.CharField(max_length=9)),
                ('pelTitulo', models.CharField(max_length=50)),
                ('pelProtagonista', models.CharField(max_length=50)),
                ('pelDuracion', models.IntegerField()),
                ('pelResumen', models.CharField(max_length=2000)),
                ('pelFoto', models.ImageField(
                    blank=True, null=True, upload_to='fotos/')),
                ('pelGenero', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='appPeliculas.genero')),
            ],
        ),
    ]