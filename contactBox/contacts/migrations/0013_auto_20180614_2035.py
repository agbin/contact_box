# Generated by Django 2.0.6 on 2018-06-14 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0012_auto_20180614_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='type',
            field=models.CharField(choices=[('HOME', 'home'), ('BUSINESS', 'business')], max_length=8),
        ),
    ]
