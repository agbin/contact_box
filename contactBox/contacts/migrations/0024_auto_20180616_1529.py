# Generated by Django 2.0.6 on 2018-06-16 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0023_auto_20180616_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='person',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='person',
        ),
        migrations.DeleteModel(
            name='Email',
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
    ]
