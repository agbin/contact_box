# Generated by Django 2.0.6 on 2018-06-12 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_auto_20180612_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(max_length=96),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(db_index=True, max_length=254),
        ),
    ]
