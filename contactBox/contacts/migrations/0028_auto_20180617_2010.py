# Generated by Django 2.0.6 on 2018-06-17 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0027_auto_20180616_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='type',
            field=models.CharField(choices=[('HOME', 'home'), ('BUSINESS', 'business')], max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='type',
            field=models.CharField(choices=[('HOME', 'home'), ('BUSINESS', 'business')], max_length=8, null=True),
        ),
    ]
