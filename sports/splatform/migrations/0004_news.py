# Generated by Django 3.2 on 2021-05-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splatform', '0003_team_point'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(default=0, verbose_name='新闻编号')),
                ('url', models.CharField(max_length=999, verbose_name='新闻地址')),
            ],
            options={
                'verbose_name_plural': '新闻表',
            },
        ),
    ]
