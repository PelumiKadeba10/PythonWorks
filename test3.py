# this snippet edits data in a json file....
import json

pwords = {'rest': 'jdj', 'ddd': 'dhdh', 'dda': 'daad'}
with open('test.json', 'w') as f:
    json.dump(pwords, f, indent=4)


def remove(path, x):
    x = str(x)
    with open(path, 'r') as f:
        oops = json.load(f)
    if x in oops.keys():
        oops.pop(x)
    # writing the new updated dictionary back into the file
    with open(path, 'w') as g:
        json.dump(oops, g, indent=4)
    with open(path, 'r') as w:
        oops = json.load(w)
        for keys, values in oops.items():
            print(f'{keys}: {values}')

remove('test.json', 'rest')