# Generated by Django 4.1.3 on 2022-11-07 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ru_name', models.CharField(max_length=150)),
                ('eng_name', models.CharField(max_length=150)),
                ('alt_name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('tags', models.ManyToManyField(to='book.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.FloatField()),
                ('number', models.IntegerField()),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.title')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('content', models.TextField()),
                ('views_counter', models.IntegerField()),
                ('like_counter', models.IntegerField()),
                ('volume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.volume')),
            ],
        ),
    ]
