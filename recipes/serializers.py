from rest_framework import serializers

from .exceptions.api_exceptions import IngredientNotFound
from .models import Ingredient, Recipe, RecipeIngredient


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'unit']


class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeIngredient
        fields = ['id', 'ingredient', 'quantity']


class RecipeSerializer(serializers.ModelSerializer):
    recipe_ingredients = RecipeIngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = [
            'id', 'name', 'preparation_time_minutes', 'recipe_ingredients'
        ]


class RecipeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'preparation_time_minutes']


class AddIngredientToRecipeSerializer(serializers.Serializer):
    ingredient_id = serializers.IntegerField()
    quantity = serializers.FloatField()

    def validate(self, data):
        ingredient_id = data.get('ingredient_id')
        quantity = data.get('quantity')

        try:
            Ingredient.objects.get(id=ingredient_id)
        except Ingredient.DoesNotExist:
            raise IngredientNotFound()

        if quantity <= 0:
            raise serializers.ValidationError(
                {'quantity': 'Quantity must be greater than 0'})

        return data
