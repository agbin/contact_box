# Generated by Django 2.0.6 on 2018-06-16 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0026_auto_20180616_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
