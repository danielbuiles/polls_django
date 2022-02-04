# Generated by Django 4.0rc1 on 2022-02-04 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Opciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.preguntas')),
            ],
        ),
    ]
