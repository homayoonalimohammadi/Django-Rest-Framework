# Generated by Django 4.0.3 on 2022-03-24 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Snippets',
            new_name='Snippet',
        ),
    ]
