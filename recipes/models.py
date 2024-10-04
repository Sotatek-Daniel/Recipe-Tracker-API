from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Ingredient(BaseModel):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recipe(BaseModel):
    name = models.CharField(max_length=255)
    preparation_time_minutes = models.IntegerField()

    def __str__(self):
        return self.name


class RecipeIngredient(BaseModel):
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               related_name='recipe_ingredients')
    ingredient = models.ForeignKey(Ingredient,
                                   on_delete=models.CASCADE,
                                   related_name='ingredient_recipes')
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.quantity} {self.ingredient.unit} of {self.ingredient.name} in {self.recipe.name}"
