# Generated by Django 2.1.4 on 2019-12-26 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='sex',
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.CharField(default='default', max_length=128),
        ),
    ]
