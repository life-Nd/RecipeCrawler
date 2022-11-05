from meal_db_recipe_model import MealDbRecipeModel

"""
Write another class called RecipeParser with a function processRecipe that receives a parameter of type Recipe and maps it to following variable:
sourceId
title
area
difficulty
duration
uid
category
sub_category
stars
used_count
ingredients_count
steps_count
tags
youtube
image_url
reference
reviews_count
made
portions
likedBy
username
diet
tags
language
userphoto

For the variables created in the RecipeParser class but not in the Recipe class. Write functions to query the value missing from website like wikipedia.com

"""


class MyxmiRecipeModel:
    def __init__(self, sourceId, title, area, category, ingredients, ingredients_count, instructions, instructions_count, tags, youtube, language, stars, reviews_count, used_count, likedBy, difficulty, duration, portions, uid, image_url, made, username, diet, userphoto):
        self.sourceId = sourceId
        self.title = title
        self.area = area
        self.category = category
        self.ingredients = ingredients
        self.ingredients_count = ingredients_count
        self.instructions = instructions
        self.instructions_count = instructions_count
        self.tags = tags
        self.youtube = youtube
        self.language = language
        self.stars = stars
        self.reviews_count = reviews_count
        self.used_count = used_count
        self.likedBy = likedBy
        self.difficulty = difficulty
        self.duration = duration
        self.portions = portions
        self.uid = uid
        self.image_url = image_url
        self.made = made
        self.username = username
        self.diet = diet
        self.userphoto = userphoto

    @classmethod
    def fromMealDbRecipe(cls, mealDbRecipe: MealDbRecipeModel):
        return cls(
            sourceId=mealDbRecipe.idMeal,
            title=mealDbRecipe.strMeal,
            area=mealDbRecipe.strArea,
            category=mealDbRecipe.strCategory,
            ingredients=mealDbRecipe.ingredients,
            ingredients_count=len(mealDbRecipe.ingredients),
            instructions=mealDbRecipe.instructions,
            instructions_count=len(mealDbRecipe.instructions),
            tags=mealDbRecipe.strYoutube,
            youtube=mealDbRecipe.strMealThumb,
            language='English',
            username='',
            userphoto='',
            stars=0,
            reviews_count=0,
            used_count=1,
            likedBy=[],
            difficulty='',
            duration='',
            portions='',
            diet='',
            uid='',
            image_url='',
            made='',
            )
