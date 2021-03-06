# Generated by Django 3.2 on 2022-05-08 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='type de bien')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='prix')),
            ],
            options={
                'verbose_name': 'bien',
                'verbose_name_plural': 'bien',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nom')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=25, verbose_name='Téléphone')),
                ('subject', models.CharField(max_length=150, verbose_name='sujet')),
                ('message', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='Formule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formule', models.CharField(max_length=150, verbose_name='Pack nettoyage')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='prix')),
                ('description', models.TextField(verbose_name='Descriptions du pack')),
            ],
            options={
                'verbose_name': 'formule',
                'verbose_name_plural': 'formules',
            },
        ),
        migrations.CreateModel(
            name='Hiring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nom')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=25, verbose_name='Téléphone')),
                ('birth_date', models.DateField()),
                ('birth_place', models.CharField(max_length=150, verbose_name='lieu de naissance')),
                ('message', models.TextField(verbose_name='experience')),
                ('cv_file', models.FileField(blank=True, null=True, upload_to='media', verbose_name='CV')),
            ],
            options={
                'verbose_name': 'hiring',
                'verbose_name_plural': 'hirings',
            },
        ),
        migrations.CreateModel(
            name='Surface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surface', models.CharField(max_length=25, verbose_name='surface en m2')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='prix')),
            ],
            options={
                'verbose_name': 'bien',
                'verbose_name_plural': 'bien',
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=25, verbose_name='Téléphone')),
                ('bien', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.bien')),
                ('formule', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.formule')),
                ('surface', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.surface')),
            ],
            options={
                'verbose_name': 'quote',
                'verbose_name_plural': 'quotes',
            },
        ),
    ]
