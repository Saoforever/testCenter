import json 

myDictionary = {
    "name": "Mike",
    "age": 26,
    "favorite_color": "Purple",
    "hobbies": ["coding", "gaming"],
}

print(json.dumps(myDictionary))

with open("data.json", "w") as file_pointer:
    json.dump(myDictionary, file_pointer, indent=4)

with open("data.json", "r") as file_reader:
    print(file_reader.read())
