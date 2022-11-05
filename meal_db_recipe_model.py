"""
Generate the code for a python class called Recipe with a function fronJson that receives a parameter of type json and maps it to following variable:
idMeal
idMeal
strMeal
strCategory
strArea
strInstructions
strMealThumb
strTags
strYoutube
ingredients
"""

import requests

class MealDbRecipeModel:
    def __init__(self, idMeal, strMeal, strCategory, strArea, strMealThumb, strTags, strYoutube, ingredients, instructions):
        self.idMeal = idMeal
        self.strMeal = strMeal
        self.strCategory = strCategory
        self.strArea = strArea
        self.strMealThumb = strMealThumb
        self.strTags = strTags
        self.strYoutube = strYoutube
        self.ingredients = ingredients
        self.instructions = instructions

    """
    Write a function called fetchOnline that queries the API of a website like wikipedia
    """
    @classmethod
    def queryApiMealDb(letter):
        # TODO change this for the url
        # response = request.get('https://www.themealdb.com/api/json/v1/1/random.php')
        api_meal_url = F'https://www.themealdb.com/api/json/v1/1/search.php?f='+letter
        response = requests.get(api_meal_url)
        return response.json()

    @classmethod
    def parseIngredients(cls, jsonData):
        ingredients = {}
        for key in jsonData:
            if(key.startswith("strIngredient")):
                length = len(key)
                index = key[13:length]
                notEmpty = jsonData[key] != ""
                notNone = jsonData[key] != "None"
                if(notEmpty and notNone):
                    ingredientName = jsonData[key]
                    ingredientMeasure = jsonData[F"strMeasure{index}"]
                    ingredients[ingredientName] = ingredientMeasure
        return ingredients

    @classmethod
    def parseInstructions(cls, strInstructions):
        instructions = str(strInstructions).splitlines()
        return instructions

    @classmethod
    def fromJson(cls, jsonData):
        return cls(idMeal=jsonData['idMeal'],
                   strMeal=jsonData['strMeal'],
                   strCategory=jsonData['strCategory'],
                   strArea=jsonData['strArea'],
                   strMealThumb=jsonData['strMealThumb'],
                   strTags=jsonData['strTags'],
                   strYoutube=jsonData['strYoutube'],
                   ingredients=cls.parseIngredients(jsonData),
                   instructions=cls.parseInstructions(jsonData['strInstructions']),)
