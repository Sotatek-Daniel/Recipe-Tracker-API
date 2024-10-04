from django.urls import path

from .views import (AddIngredientToRecipeView, IngredientViewSet,
                    RecipeListCreateView)

urlpatterns = [
    path('', RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('<int:recipe_id>/',
         AddIngredientToRecipeView.as_view(),
         name='add-ingredient-to-recipe'),
    path('ingredient/',
         IngredientViewSet.as_view(),
         name='add-ingredient-to-recipe'),
]
