import requests
import json


print("\nPlease enter one of the following:\n----------------------------------\n - Jackets\n - Shirts\n - Tops/Sweaters\n - Sweatshirts\n - Shorts\n - Hats\n - Bags\n - Accessories\n - Shoes\n - Skate")

def getInput():
    category = input("\nSelection: ")
    return category

category = getInput()

while category.lower() != "jackets" and category.lower() != "shirts" and category.lower() != "tops/sweaters" and category.lower() != "sweatshirts" and category.lower() != "shorts" and category.lower() != "hats" and category.lower() != "bags" and category.lower() != "accessories" and category.lower() != "shoes" and category.lower() != "skate":
    print("Please check spelling")
    category = getInput()



url = "https://www.supremenewyork.com/shop.json"

r = requests.request("get", url=url)

r = requests.get(url)
jsonText = json.loads(r.text)

category = category.title()

print("\nThe following procuts are live:\n-------------------------------")
i = 0
while i < len(jsonText['products_and_categories'][category]):
    item = ("["+jsonText['products_and_categories'][category][i]['name']+"]")
    link = (" https://www.supremenewyork.com/shop/"+category+"/"+str(jsonText['products_and_categories'][category][i]['id']))
    print(item + link)
    i+=1

# https://www.supremenewyork.com/shop/category/id