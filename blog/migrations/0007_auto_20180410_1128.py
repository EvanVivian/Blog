# Generated by Django 2.0 on 2018-04-10 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_readed_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='readed_num',
            field=models.IntegerField(default=0, verbose_name='阅读次数'),
        ),
    ]
