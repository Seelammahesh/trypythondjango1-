# Generated by Django 4.2.6 on 2023-11-03 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_recipeingredientimage_extracted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredients',
            name='quantity',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
