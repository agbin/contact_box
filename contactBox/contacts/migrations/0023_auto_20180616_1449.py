# Generated by Django 2.0.6 on 2018-06-16 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0022_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='member',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
