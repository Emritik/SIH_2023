# Generated by Django 2.2.12 on 2023-09-24 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_uploaddata_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectupdate',
            name='ids',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='projectupdate',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
