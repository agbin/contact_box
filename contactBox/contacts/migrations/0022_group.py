# Generated by Django 2.0.6 on 2018-06-16 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0021_auto_20180615_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=30)),
                ('member', models.ManyToManyField(blank=True, to='contacts.Person')),
            ],
        ),
    ]