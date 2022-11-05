from array import array
import json
import string
import requests
from meal_db_recipe_model import MealDbRecipeModel
from recipe_parser import RecipeParser
from myxmi_recipe_model import MyxmiRecipeModel


class Crawler():
    def __init__(self):
        print("--------------------------")
        print("Crawler  initializing...")


def queryLocalMealDb(fileName):
    with open(fileName+'.json', 'r') as file:
        return file.read()

def saveFromLocalToLocal():
    dataStr = queryLocalMealDb("recipe")
    dataJson = json.loads(dataStr)
    saveToLocal(dataJson)


def saveToLocal(dataJson: list):
    with open('myxmi_recipe_local'+'.json', 'a') as file:
        recipesToUpload = []
        for data in dataJson:
            mealDbLocalJson = MealDbRecipeModel.fromJson(data)
            print('✅  Saved: ', mealDbLocalJson.idMeal,'recipe_local.json')
            myxmiRecipe = MyxmiRecipeModel.fromMealDbRecipe(mealDbLocalJson)
            recipesToUpload.append(myxmiRecipe.__dict__)
        json.dump(recipesToUpload, file, indent=4,)


def queryMealDbApi(letter):
    api_meal_url = F'https://www.themealdb.com/api/json/v1/1/search.php?f='+letter
    response = requests.get(api_meal_url)
    if (response.status_code == 200):
            jsonData = response.json()        
            return jsonData


def saveFromApiToLocal():
    letters = list(string.ascii_lowercase)
    mealsList=[]
    
    for letter in letters:
            print(f'----------------{letter= }----------------')
            jsonData = queryMealDbApi(letter)
            mealsByLetter =jsonData["meals"]
            if(mealsByLetter):
                print(F'{mealsByLetter= }')
                mealsList.extend(mealsByLetter)
                
            
    saveToLocal(mealsList)

if __name__ == "__main__":
    print("-------------Crawler initialized-------------")
    saveFromApiToLocal()
