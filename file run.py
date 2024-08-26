import json
import os

x = str(input())
y = str(input())
file_path = 'test.json'

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        pwords = json.load(file)
else:
    pwords = {}

pwords[x] = y
with open(file_path, 'w') as file:
    json.dump(pwords, file, indent=4)

with open(file_path, 'r') as file:
    data = json.load(file)
    for key, value in data.items():
        print(f'{key}:{value}')
    # print(json.dumps(data))   # displays the whole data as it is from the file




