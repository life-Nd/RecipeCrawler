# from firebase_admin import firestore
import requests  # to get image from the web
import shutil 
from typing import Collection
from firebase_admin import credentials, initialize_app, storage, firestore
import datetime


class FirestoreServicesHelper:
    @staticmethod
    def upload_image(_imageName, raw):
        with open(_imageName, "wb") as f:
            shutil.copyfileobj(raw, f)
            if (_imageName != "None"):
                bucket = storage.bucket()
                blob = bucket.blob(_imageName)
                blob.upload_from_filename(_imageName)
                blob.make_public()
                blob_url = blob.public_url
                print("Image sucessfully Public: ", blob_url)
                recipe_url = blob.public_url
                return recipe_url
    
    @staticmethod
    def read_data(id, _image_url, diet, sub_category):
        _ingredients = {}
        _mealDetailsUrl = F"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}"
        requestMealsDetailsInUrl = requests.get(_mealDetailsUrl)
        if (requestMealsDetailsInUrl.status_code == 200):
            _jsonUrlData = requestMealsDetailsInUrl.json()
            dataList = _jsonUrlData["meals"]
            for data in dataList:
                for _key in data.keys():
                    if(_key.startswith("strIngredient")):
                        _index = _key[13:len(_key)]
                        if(data[_key] != "" and data[_key] != "None"):
                            _ingredients[data[_key]
                                         ] = data[F"strMeasure{_index}"]
                _id = data["idMeal"]
                _title = str(data["strMeal"]).lower()
                _category = str(data["strCategory"]).lower()
                print("_category", _category)

                _area = str(data["strArea"])
                _steps = str(data["strInstructions"]).split(".")
                _tagsMap = {{_category: True}, {
                    sub_category: True}, {diet: True},
                },
                _tagsList = str(data["strTags"]).lower().split(
                    ",")
                for _tag in _tagsList:
                    _tagsMap[_tag] = True
                _youtube = data["strYoutube"]
                _strMealThumbnail = data["strMealThumb"]
                _strSource = data["strSource"]
                _milliseconds = int(
                    datetime.datetime.now().strftime("%s")) * 1000
                _made = F"{_milliseconds}"
                # TODO Changed tags to contain category,subcategory and diet
                details = {
                    "access": "public",
                    # "category": _category,
                    "title": _title,
                    "area": _area,
                    "difficulty": "medium",
                    "duration": "25 min",
                    "uid": "xQkQZgUlYYedGxgsBLRNCmzQcok2",
                    "category": "food",
                    # "sub_category": sub_category,
                    "stars": "None",
                    "used_count": "1",
                    "ingredients_count": str(len(_ingredients)),
                    "steps_count": str(len(_steps)),
                    "tags": _tagsMap,
                    "youtube": _youtube,
                    "image_url": _image_url,
                    "reference": _id,
                    "reviews_count": "0",
                    "made": _made,
                    "portions": "4",
                    "likedBy": [],
                    "username": "MealDB",
                    "userphoto": "https://firebasestorage.googleapis.com/v0/b/myxmi-94982.appspot.com/o/ic_launcher-playstore.png?alt=media&token=9c788b68-16fd-4c38-a7c6-a8f372eadd10",
                    # "diet": diet,
                    # "tags": _tags,
                    "language": "en",
                }
                instructions = {
                    "steps": _steps,
                    "ingredients": _ingredients,
                    "reviews": [],
                    "url": _strSource,
                    "thumbnailSource": _strMealThumbnail
                }

            if(details["ingredients_count"] != "None" and instructions["steps"] != "None"):
                _imported = ["", ""]
                if(_imported.__contains__(details["title"])):
                    print(details, instructions)
                else:
                    save_data(details, instructions)


def save_data(details, instructions):
    print("=====running=====-----save_data-----",)
    db = firestore.client()
    ref = db.collection("Recipes").document()
    ref.set(details)
    print("doc_ref", ref.id)
    if (ref.id != "None"):
        db.collection(u"Instructions").document(
            ref.id).set(instructions)

    # FIX THIS
    # NOT BEING ABLE TO GO PAST THIS POINT
    # for _dict in data:
    #     _dict_keys = _dict
    #     print("data.keys:", _dict_keys)
    #     print("_dict:", type(_dict))
    #     print("item:", _dict["strMeal"])
    #     _strIngredient = "strIngredient"
    #     if(_dict_keys.startswith(_strIngredient)):
    #         _index = _dict_keys[13:len(_dict_keys)]
    #         print("index:", _index)
    #         if(data[_dict_keys] != "" and data[_dict_keys] != "None"):
    #             _ingredients[data[_dict_keys]
    #                          ] = data[F"strMeasure{_index}"]
    #             _id = data["idMeal"]
    #             print("_id", _id)
    #             _title = str(data["strMeal"]).lower()
    #             _category = str(data["strCategory"]).lower()
    #             print("_category", _category)
    #             _area = str(data["strArea"])
    #             _steps = data["strInstructions"]
    #             _tags = data["strTags"]
    #             _youtube = data["strYoutube"]
    #             _strMealThumbnail = data["strMealThumb"]
    #             _strSource = data["strSource"]
    #             _image_url = _image_url
    #             details = {
    #                 "access": "public",
    #                 "category": _category,
    #                 "title": _title,
    #                 "area": _area,
    #                 "difficulty": "medium",
    #                 "duration": "30 min",
    #                 "image_url": _image_url,
    #                 "uid": "xQkQZgUlYYedGxgsBLRNCmzQcok2",
    #                 "category": "food",
    #                 "sub_category": "salad",
    #                 "stars": "None",
    #                 "used_count": "1",
    #                 "ingredients_count": len(_ingredients),
    #                 "steps_count": len(_steps),
    #                 "tags": _tags,
    #                 "youtube": _youtube,
    #                 "imageUrl": _image_url,
    #                 "reference": _id,
    #                 "reviewsCount": "0.0",
    #                 "made": "",
    #                 "portions": "1",
    #                 "likedBy": "None",
    #                 "username": "Ralph",
    #                 "photoUrl": "https://firebasestorage.googleapis.com/v0/b/myxmi-94982.appspot.com/o/1633484360052-15857.jpg?alt=media&token=858e6507-d2ad-4f17-a441-333ccd4bb740",
    #                 "diet": "vegan",
    #                 "tags": _tags,
    #                 "language": "en",
    # }
    #         instructions = {
    #             "title": _title,
    #             "steps": _steps,
    #             "ingredients": _ingredients,
    #             "reviews": [],
    #             "url": _strSource,
    #             "thumbnailSource": _strMealThumbnail
    #         }
    #         print("details:", details)
    #         print("instructions:", instructions)
    # ref = db.collection("Recipes").document()
    # ref.set(details)
    # print("doc_ref", ref.id)
    # if (ref.id != "None"):
    #     db.collection(u"Instructions").document(
    #         ref.id).set(instructions)
