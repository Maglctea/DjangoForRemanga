# Generated by Django 4.1.3 on 2022-11-07 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='alt_name',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
