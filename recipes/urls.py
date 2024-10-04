from django.urls import path

from .views import AddIngredientToRecipeView, RecipeListCreateView

urlpatterns = [
    path('', RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('<int:recipe_id>/add-ingredient/',
         AddIngredientToRecipeView.as_view(),
         name='add-ingredient-to-recipe'),
]
