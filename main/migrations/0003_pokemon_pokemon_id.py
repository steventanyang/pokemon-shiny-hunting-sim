# Generated by Django 4.2.3 on 2023-08-02 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_pokedex_pokemon_region_delete_item_delete_todolist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='pokemon_id',
            field=models.IntegerField(default=0),
        ),
    ]
