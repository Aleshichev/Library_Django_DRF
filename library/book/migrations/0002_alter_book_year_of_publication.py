# Generated by Django 4.1 on 2023-07-09 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year_of_publication',
            field=models.IntegerField(default=None),
        ),
    ]
