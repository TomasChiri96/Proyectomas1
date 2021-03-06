# Generated by Django 4.0.3 on 2022-04-21 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='almancen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=20, verbose_name='producto')),
                ('stock', models.BooleanField(verbose_name='stock')),
            ],
        ),
        migrations.CreateModel(
            name='mesas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_mesa', models.IntegerField(verbose_name='numero mesa')),
                ('mesa_libre', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='mozo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=20, verbose_name='apellido')),
                ('numero', models.IntegerField(verbose_name='numero')),
            ],
        ),
    ]
