# Generated by Django 2.0 on 2018-04-14 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20180413_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent_id',
            field=models.IntegerField(default=0),
        ),
    ]
