# Generated by Django 2.1.1 on 2018-09-25 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0030_auto_20180925_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='emails', to='contacts.Person'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='phones', to='contacts.Person'),
        ),
    ]