# Generated by Django 4.1.3 on 2022-11-09 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_chapter_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='like_counter',
            field=models.PositiveIntegerField(default=0, verbose_name='Кол-во лайков'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='number',
            field=models.PositiveIntegerField(verbose_name='Номер главы'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='views_counter',
            field=models.PositiveIntegerField(default=0, verbose_name='Кол-во просмотров'),
        ),
        migrations.AlterField(
            model_name='volume',
            name='number',
            field=models.PositiveIntegerField(verbose_name='Номер тома'),
        ),
        migrations.AlterField(
            model_name='volume',
            name='price',
            field=models.PositiveBigIntegerField(default=0, verbose_name='Цена'),
        ),
    ]