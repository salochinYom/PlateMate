"""This file is used to create classes for the dataset to use with the analyzers"""

from models.meal_plan import MealPlan, Recipe, Ingredient, Nutrition, Vitamin
import pandas as pd
from typing import List
import ast


class Dataset:
    def __init__(self, recipes: List[Recipe] = None, ingredients: List[Ingredient]=None, meal_plans: List[MealPlan]=None):
        
        self.recipes = recipes
        self.ingredients = ingredients
        self.meal_plans = meal_plans

    def get_recipe_by_title(self, title: str) -> Recipe:
        for recipe in self.recipes:
            if recipe.title == title:
                return recipe
        return None

    def get_ingredient_by_name(self, name: str) -> Ingredient:
        for ingredient in self.ingredients:
            if ingredient.name == name:
                return ingredient
        return None

    def get_meal_plan_by_title(self, title: str) -> MealPlan:
        for meal_plan in self.meal_plans:
            if meal_plan.title == title:
                return meal_plan
        return None
    
    def create_recipes_from_csv(self, file_path: str="data/recipes/full_dataset.csv"):
        recipes = []
        df = pd.read_csv(file_path, delimiter=',', encoding='utf-8')
        for index, row in df.iterrows():
            recipe_number = 0
            title = row['title']
            #converts string to list
            ingredients = ast.literal_eval(row['ingredients'])
            directions = row['directions']
            link = row['link']
            source = row['source']
            NER = ast.literal_eval(row['NER'])
            #TODO links to ingredients
            recipe = Recipe(recipe_number, title, ingredients, directions, link, source, NER)
            recipes.append(recipe)
        self.recipes = recipes



class IngredientsDataset:
    def __init__(self, ingredients: List[Ingredient] = None):
        self.ingredients = ingredients

    def get_ingredient_by_name(self, name: str) -> Ingredient:
        for ingredient in self.ingredients:
            if ingredient.name == name:
                return ingredient
        return None

    def create_ingredients_from_csv(self, file_path: str="data/recipes/full_dataset.csv"):
        ingredients = []
        df = pd.read_csv(file_path, delimiter=',', encoding='utf-8')
        for index, row in df.iterrows():
            name = row['name']
            nutrition = Nutrition(row['calories'], [Vitamin(row['vitamin'], row['amount'], row['unit'])])
            cost_per_weight = row['cost_per_weight']
            ingredient = Ingredient(name, nutrition, cost_per_weight)
            ingredients.append(ingredient)
        self.ingredients = ingredients
        
