# Generated by Django 3.2 on 2022-05-08 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0007_alter_surface_surface'),
    ]

    operations = [
        migrations.AddField(
            model_name='surface',
            name='unite',
            field=models.IntegerField(blank=True, null=True, verbose_name='prix unitaire'),
        ),
    ]