# Generated by Django 3.2 on 2022-05-16 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0019_auto_20220516_0905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='about_high_en',
            new_name='about_high_ar_dz',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='name_en',
            new_name='name_ar_dz',
        ),
    ]