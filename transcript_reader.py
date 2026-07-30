import json

results = {}

with open("sample.txt", "r") as song:
    lines = song.readlines()
    print(lines)
    for index, line in enumerate(lines):

        results[index + 1] = line.strip()

with open("file_data.json", "w") as file_pointers:
    json.dump(results, file_pointers)