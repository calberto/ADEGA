# Generated by Django 5.1.2 on 2024-10-12 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=255)),
                ('categoria', models.CharField(max_length=50)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('imagem', models.ImageField(upload_to='media/imagens/')),
            ],
        ),
        migrations.CreateModel(
            name='Uva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=255)),
                ('imagem', models.ImageField(upload_to='media/imagens/')),
            ],
        ),
        migrations.CreateModel(
            name='Vinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('teorAlc', models.CharField(max_length=50)),
                ('tempAmbServ', models.CharField(max_length=50)),
                ('data', models.DateField()),
                ('local', models.CharField(max_length=50)),
                ('safra', models.CharField(max_length=50)),
                ('produtor', models.CharField(max_length=100)),
                ('paisRegiao', models.CharField(max_length=100)),
                ('degustador', models.CharField(max_length=1000)),
                ('rotulo', models.CharField(max_length=255)),
                ('uva_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.uva')),
            ],
        ),
    ]
