# Generated by Django 4.2.6 on 2023-10-27 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_alter_recipeingredients_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredients',
            name='quantity_as_float',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
