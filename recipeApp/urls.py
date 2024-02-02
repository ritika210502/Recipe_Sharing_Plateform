from django.urls import path
from recipeApp import views
urlpatterns = [
    path('',views.login_page,name="recipe"),
    path('recipe/',views.recipe,name="recipe"),
    path('deleteRecipe/<id>/',views.deleteRecipe,name="deleteRecipe"),
    path('updateRecipe/<id>/',views.updateRecipe,name="updateRecipe"),

]