# Generated by Django 2.2.12 on 2023-09-24 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20230924_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectupdate',
            name='ids',
        ),
    ]
