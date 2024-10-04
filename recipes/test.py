from unittest.mock import patch

from django.test import TestCase

from .exceptions.api_exceptions import IngredientNotFound
from .models import Ingredient
from .serializers import AddIngredientToRecipeSerializer


class AddIngredientToRecipeSerializerTest(TestCase):

    @patch('recipes.serializers.Ingredient.objects.get')
    def test_validate_ingredient_id_success(self, mock_get):
        mock_get.return_value = Ingredient(id=1, name="Sugar", unit="grams")

        data = {'ingredient_id': 1, 'quantity': 100.0}

        serializer = AddIngredientToRecipeSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['ingredient_id'], 1)
        self.assertEqual(serializer.validated_data['quantity'], 100.0)

    @patch('recipes.serializers.Ingredient.objects.get')
    def test_validate_ingredient_id_not_found(self, mock_get):
        mock_get.side_effect = Ingredient.DoesNotExist

        data = {'ingredient_id': 999, 'quantity': 100.0}

        serializer = AddIngredientToRecipeSerializer(data=data)
        with self.assertRaises(IngredientNotFound):
            serializer.is_valid(raise_exception=True)

    @patch('recipes.serializers.Ingredient.objects.get')
    def test_invalid_quantity(self, mock_get):
        mock_get.return_value = Ingredient(id=1, name="Sugar", unit="grams")

        data = {'ingredient_id': 1, 'quantity': -50.0}

        serializer = AddIngredientToRecipeSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('quantity', serializer.errors)
