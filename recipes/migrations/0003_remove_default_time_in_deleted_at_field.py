# Generated by Django 5.1.1 on 2024-10-03 19:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0002_add_soft_delete_and_created_at_updated_at_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="ingredient",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="recipe",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="recipeingredient",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
    ]
