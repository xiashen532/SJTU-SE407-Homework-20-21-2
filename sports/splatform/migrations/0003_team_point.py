# Generated by Django 3.2 on 2021-05-05 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splatform', '0002_auto_20210503_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='point',
            field=models.IntegerField(default=0, verbose_name='积分'),
        ),
    ]