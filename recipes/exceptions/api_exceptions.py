from rest_framework import status
from rest_framework.exceptions import APIException


class RecipeNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Recipe Not Found.'
    default_code = 'RecipeNotFound'


class IngredientNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Ingredient Not Found.'
    default_code = 'IngredientNotFound'
