# Generated by Django 4.1.5 on 2023-01-13 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='tittle',
            new_name='title',
        ),
    ]
