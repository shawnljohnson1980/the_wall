# Generated by Django 2.2.4 on 2021-04-23 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_wall_app', '0002_auto_20210422_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
