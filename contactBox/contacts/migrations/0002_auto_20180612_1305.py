# Generated by Django 2.0.6 on 2018-06-12 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutperson',
            old_name='first_name',
            new_name='name1',
        ),
        migrations.RenameField(
            model_name='aboutperson',
            old_name='last_name',
            new_name='name2',
        ),
    ]
