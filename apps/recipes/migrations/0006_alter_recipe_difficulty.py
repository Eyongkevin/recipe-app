# Generated by Django 4.2.15 on 2024-09-08 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_rename_description_recipe_directions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(editable=False, max_length=20),
        ),
    ]
