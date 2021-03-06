# Generated by Django 3.2 on 2022-05-15 10:11

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0014_auto_20220515_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name="Nom de l'entreprise")),
                ('image_high', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='img_1')),
                ('image_low', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='img_1')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Titre')),
                ('about_high', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text a propos')),
                ('about_low', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Page dossier taksit')),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
            },
        ),
        migrations.AlterField(
            model_name='business',
            name='folder_page',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name="Page d'accueil"),
        ),
    ]
