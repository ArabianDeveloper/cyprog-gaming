# Generated by Django 4.1.5 on 2023-01-23 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_game_data_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='storage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
