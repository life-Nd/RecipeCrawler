import csv
import json
import sqlite3
from xml.dom.minidom import Element
from xml.etree import ElementTree
from xml.etree.ElementTree import SubElement
from api_keys import ApiKeys
from myxmi_recipe_model import MyxmiRecipeModel
import requests


"""
Write another class called RecipeParser with a function processRecipe that receives a parameter of type Recipe and maps it to following variable:
mealDbId
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

class RecipeParser:
    def __init__(self, mealDbId, title, area, difficulty, duration, uid, category, sub_category, stars, used_count, ingredients_count, steps_count, tags, youtube, image_url, reference, reviews_count, made, portions, likedBy, username, diet, language, userphoto, ingredients
                 ):
        self.mealDbId = mealDbId
        self.title = title
        self.area = area
        self.difficulty = difficulty
        self.duration = duration
        self.uid = uid
        self.category = category
        self.sub_category = sub_category
        self.stars = stars
        self.used_count = used_count
        self.ingredients_count = ingredients_count
        self.steps_count = steps_count
        self.tags = tags
        self.youtube = youtube
        self.image_url = image_url
        self.reference = reference
        self.reviews_count = reviews_count
        self.made = made
        self.portions = portions
        self.likedBy = likedBy
        self.username = username
        self.diet = diet
        self.tags = tags
        self.language = language
        self.userphoto = userphoto

    """
    Create an object called recipeParser from the RecipeParser class and which uses the processRecipe function to map the recipe object above
    """

    def printRecipe(recipe: MyxmiRecipeModel, action):
        print("----------------------------", action,
              "----------------------------"),
        print(f'{recipe.sourceId= }')
        print(f'{recipe.title= }')
        print(f'{recipe.area= }')
        print(f'{recipe.category= }')
        print(f'{recipe.ingredients= }')
        print(f'{recipe.ingredients_count= }')
        print(f'{recipe.instructions= }')
        print(f'{recipe.instructions_count= }')
        print(f'{recipe.tags= }')
        print(f'{recipe.youtube= }')
        print(f'{recipe.language= }')
        print(f'{recipe.stars= }')
        print(f'{recipe.reviews_count= }')
        print(f'{recipe.used_count= }')
        print(f'{recipe.likedBy= }')
        print(f'{recipe.difficulty= }')
        print(f'{recipe.duration= }')
        print(f'{recipe.portions= }')
        print(f'{recipe.uid= }')
        print(f'{recipe.image_url= }')
        print(f'{recipe.made= }')
        print(f'{recipe.username= }')
        print(f'{recipe.diet= }')
        print(f'{recipe.userphoto= }')
        print("---------------------------------------------------------------")

    """
    Write a function called writeToFile that receives a parameter of type RecipeParser and writes it to a file called recipe.txt
    """

    def writeToJSON(fileName, recipe: MyxmiRecipeModel):
        with open(fileName+'.json', 'a') as file:
            json.dump(recipe.__dict__, file, indent=4)
            print(F'✅  Saved {recipe.title}.json')

    """
    Write a function called readFromJSON that reads a file called recipe.json and returns an object of type RecipeParser
    """

    def readFromJSON(fileName):
        with open(fileName+'.json', 'r') as file:
            return MyxmiRecipeModel(**json.load(file))

    def writeToTxtFile(recipe, fileName):
        with open(fileName, '.txt', 'a') as file:
            file.write('\n')
            file.write(f'{str(recipe.mealDbId)}')
            file.write('\n')
            file.write(f'{recipe.title=}')
            file.write('\n')
            file.write(f'{recipe.area=}')
            file.write('\n')
            file.write(f'{recipe.category=}')
            file.write('\n')
            file.write(f'{recipe.difficulty=}')
            file.write('\n')
            file.write(f'{recipe.duration=}')
            file.write('\n')
            file.write(f'{recipe.image_url=}')
            file.write('\n')
            file.write(f'{str(recipe.ingredients_count)}')
            file.write('\n')
            file.write(f'{recipe.language=}')
            file.write('\n')
            file.write(f'{recipe.made=}')
            file.write('\n')
            file.write(f'{recipe.portions=}')
            file.write('\n')
            file.write(f'{recipe.sub_category=}')
            file.write('\n')
            file.write(f'{recipe.tags=}')
            file.write('\n')
            file.write(f'{str(recipe.uid)=}')
            file.write('\n')
            file.write(f'{recipe.userphoto=}')
            file.write('\n')
            file.write(f'{recipe.username=}')
            file.write('\n')
            file.write(f'{str(recipe.used_count)}')
            file.write('\n')
            file.write(f'{recipe.youtube=}')

    """
    Write a function called readFromFile that reads a file called recipe.txt and returns an object of type RecipeParser
    """

    def readFromTxtFile(fileName):
        with open(fileName+'.txt', 'r') as file:
            return MyxmiRecipeModel(file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline(), file.readline())

    """
    Write a function called writeToDb that receives a parameter of type RecipeParser and writes it to a database called recipe.db
    """

    def writeToDb(fileName, recipe: MyxmiRecipeModel):
        conn = sqlite3.connect(fileName+'.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS recipe (
                        mealDbId integer,
                        title text,
                        area text,
                        difficulty text,
                        duration text,
                        uid integer,
                        category text,
                        sub_category text,
                        stars integer,
                        used_count integer,
                        ingredients_count integer,
                        steps_count text,
                        tags text,
                        youtube text,
                        image_url text,
                        reference text,
                        reviews_count integer,
                        made text,
                        portions text,
                        likedBy text,
                        username text,
                        diet text,
                        tags text,
                        language text,
                        userphoto text
                    )""")
        c.execute("INSERT INTO recipe VALUES (?,?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (recipe.sourceId, recipe.title, recipe.area, recipe.difficulty, recipe.duration, recipe.uid, recipe.category,  recipe.stars, recipe.used_count,
                  recipe.ingredients_count, recipe.instructions_count, recipe.tags, recipe.youtube, recipe.image_url, recipe.reviews_count, recipe.made, recipe.portions, recipe.likedBy, recipe.username, recipe.diet, recipe.tags, recipe.language, recipe.userphoto))
        conn.commit()
        conn.close()

    """
    Write a function called readFromDb that reads a database called recipe.db and returns an object of type RecipeParser
    """

    def readFromDb(fileName):
        conn = sqlite3.connect(fileName+'.db')
        c = conn.cursor()
        c.execute("SELECT * FROM recipe")
        row = c.fetchone()
        return MyxmiRecipeModel(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25])

    """
    Write a function called writeToJSON that receives a parameter of type RecipeParser and writes it to a file called recipe.json
    """

    """
    Write a function called writeToXML that receives a parameter of type RecipeParser and writes it to a file called recipe.xml
    """

    def writeToXML(fileName, recipe):
        recipe_element = Element('recipe')

        area = SubElement(recipe_element, 'title')
        area.text = recipe.area

        area = SubElement(recipe_element, 'area')
        area.text = recipe.area

        difficulty = SubElement(recipe_element, 'difficulty')
        difficulty.text = recipe.difficulty

        duration = SubElement(recipe_element, 'duration')
        duration.text = recipe.duration

        uid = SubElement(recipe_element, 'uid')
        uid.text = str(recipe.uid)

        category = SubElement(recipe_element, 'category')
        category.text = recipe.category

        sub_category = SubElement(recipe_element, 'sub_category')
        sub_category.text = recipe.sub_category

        stars = SubElement(recipe_element, 'stars')
        stars.text = str(recipe.stars)

        used_count = SubElement(recipe_element, 'used_count')
        used_count.text = str(recipe.used_count)

        ingredients_count = SubElement(recipe_element, 'ingredients_count')
        ingredients_count.text = str(recipe.ingredients_count)

        steps_count = SubElement(recipe_element, 'steps_count')
        steps_count.text = recipe.steps_count

        tags = SubElement(recipe_element, 'tags')
        tags.text = recipe.tags

        youtube = SubElement(recipe_element, 'youtube')
        youtube.text = recipe.youtube

        image_url = SubElement(recipe_element, 'image_url')
        image_url.text = recipe.image_url

        reference = SubElement(recipe_element, 'reference')
        reference.text = recipe.reference

        reviews_count = SubElement(recipe_element, 'reviews_count')
        reviews_count.text = str(recipe.reviews_count)

        made = SubElement(recipe_element, 'made')
        made.text = recipe.made

        portions = SubElement(recipe_element, 'portions')
        portions.text = recipe.portions

        likedBy = SubElement(recipe_element, 'likedBy')
        likedBy.text = recipe.likedBy

        username = SubElement(recipe_element, 'username')
        username.text = recipe.username

        diet = SubElement(recipe_element, 'diet')
        diet.text = recipe.diet

        tags = SubElement(recipe_element, 'tags')
        tags.text = recipe.tags

        language = SubElement(recipe_element, 'language')
        language.text = recipe.language

        userphoto = SubElement(recipe_element, 'userphoto')
        userphoto.text = recipe.userphoto

        tree = ElementTree(recipe_element)
        tree.write(fileName+'.xml')

    """
    Write a function called readFromXML that reads a file called recipe.xml and returns an object of type RecipeParser
    """

    def readFromXML(fileName):
        tree = ElementTree(file=fileName+'.xml')
        root = tree.getroot()
        return MyxmiRecipeModel(root[0].text, root[1].text, root[2].text, root[3].text, root[4].text, root[5].text, root[6].text, root[7].text, root[8].text, root[9].text, root[10].text, root[11].text, root[12].text, root[13].text, root[14].text, root[15].text, root[16].text, root[17].text, root[18].text, root[19].text, root[20].text, root[21].text, root[22].text, root[23].text, root[24].text, root[25].text)

    """
    Write a function called writeToCSV that receives a parameter of type RecipeParser and writes it to a file called recipe.csv
    """

    def writeToCSV(fileName, recipe):
        with open('recipe_processed.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['mealDbId', 'title', 'area', 'difficulty', 'duration', 'uid', 'category', 'sub_category', 'stars', 'used_count', 'ingredients_count', 'steps_count',
                            'tags', 'youtube', 'image_url', 'reference', 'reviews_count', 'made', 'portions', 'likedBy', 'username', 'diet', 'tags', 'language', 'userphoto'])
            writer.writerow([recipe.mealDbId, recipe.title, recipe.area, recipe.difficulty, recipe.duration, recipe.uid, recipe.category, recipe.sub_category, recipe.stars, recipe.used_count, recipe.ingredients_count, recipe.steps_count,
                            recipe.tags, recipe.youtube, recipe.image_url, recipe.reference, recipe.reviews_count, recipe.made, recipe.portions, recipe.likedBy, recipe.username, recipe.diet, recipe.tags, recipe.language, recipe.userphoto])

    """
    Write a function called readFromCSV that reads a file called recipe.csv and returns an object of type RecipeParser
    """

    def readFromCSV(fileName):
        with open(fileName+'recipe_processed.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            row = next(reader)
            return MyxmiRecipeModel(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25])

    # writeToFile(recipeParser)
    # newRecipeProcessed = readFromFile()

    # writeToDb(recipeParser)
    # newRecipeProcessed = readFromDb()
    # printRecipe(recipeParser)

    # writeToJSON(recipeParser)
    # newRecipeProcessed = readFromJSON()
    # printRecipe(newRecipeProcessed)

    # writeToXML(recipeParser)
    # newRecipeProcessed = readFromXML()
    # printRecipe(newRecipeProcessed)

    # writeToCSV(recipeParser)
    # newRecipeProcessed = readFromCSV()
    # printRecipe(newRecipeProcessed)

    """
    Write a function called processOnline that receives a parameter of type json and maps it to following variable:
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

    @classmethod
    def processJson(jsonData: json.JSONDecoder):
        # TODO Add the values of each missing variable
        return MyxmiRecipeModel(jsonData['meals'][0]['strArea'], 'Easy', '1:00', 0, jsonData['meals'][0]['strCategory'], '', 4, 0, len(jsonData['meals'][0]['strIngredient1']), '', jsonData['meals'][0]['strTags'], jsonData['meals'][0]['strYoutube'], jsonData['meals'][0]['strMealThumb'], '', 0, '', '', '', '', '', '', '', '', '', '')

    """
    Create an object called recipeParser from the RecipeParser class and which uses the processRecipe function to map the recipe object above
    """
    # TODO
    # queryLocal = recipe.json (1 Recipe)
    # recipeParser = processJson(queryLocal())
    # queryOnline = MealDB API
    # recipeParser = processJson(queryOnline())

    # printRecipe(recipeParser)

    """
    Write a function called askAi that queries the OpenAI Api to know the difficulty, duration, the tags,the type of sub-category, the diet type of a recipe 
    """

    def askAi(recipe: MyxmiRecipeModel):
        openai_api_key = ApiKeys.openai_api_key
        # TODO check on the OpenAI website the best prompt and settings combination for the most efficient responses.
        response = requests.get('https://api.openai.com/v1/engines/davinci/completions', headers={'Authorization': f'Bearer {openai_api_key}'}, json={'prompt': '{0} {1} {2} {3}'.format(recipe.title,recipe.area, recipe.category, recipe.tags, recipe.ingredients_count), 'max_tokens': 200, 'temperature': 0.9, 'top_p': 1, 'n': 3, 'stream': False, 'logprobs': None, 'stop': ['\n']})
        print(response.json()['choices'][0]['text'])
        print(response.json()['choices'][1]['text'])
        print(response.json()['choices'][2]['text'])
        return response.json()['choices'][0]['text']

    """
    Write a function called writeToFileAi that receives a parameter of type RecipeParser and writes it to a file called recipe.txt
    """

