# Generated by Django 4.1.5 on 2023-01-22 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_type_game_discription_game_rate_game_storage_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
    ]
