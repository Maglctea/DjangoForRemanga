# Generated by Django 4.1.3 on 2022-11-07 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_title_alt_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='like_counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='views_counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='volume',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
