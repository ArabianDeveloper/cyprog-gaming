# Generated by Django 4.1.5 on 2023-01-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='images',
        ),
        migrations.AddField(
            model_name='game',
            name='images',
            field=models.ManyToManyField(to='games.images'),
        ),
    ]
