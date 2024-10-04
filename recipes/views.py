from django.core.exceptions import ObjectDoesNotExist
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response

from .base.api_view import BaseAPIView
from .exceptions.api_exceptions import RecipeNotFound
from .models import Ingredient, Recipe, RecipeIngredient
from .serializers import (AddIngredientToRecipeSerializer,
                          RecipeCreateSerializer, RecipeSerializer)


class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RecipeCreateSerializer
        return RecipeSerializer


class AddIngredientToRecipeView(BaseAPIView):

    @swagger_auto_schema(request_body=AddIngredientToRecipeSerializer)
    def post(self, request, recipe_id):
        try:
            recipe = Recipe.objects.get(id=recipe_id)
        except ObjectDoesNotExist:
            raise RecipeNotFound
        serializer = AddIngredientToRecipeSerializer(data=request.data)
        if serializer.is_valid():
            ingredient_id = serializer.validated_data['ingredient_id']
            quantity = serializer.validated_data['quantity']

            # Get the ingredient instance
            ingredient = Ingredient.objects.get(id=ingredient_id)

            # Add the ingredient to the recipe
            RecipeIngredient.objects.create(recipe=recipe,
                                            ingredient=ingredient,
                                            quantity=quantity)

            return Response({"message": "Ingredient added successfully"},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
