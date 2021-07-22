import json

with open('game_files/locations/staiti.json') as l:
    locs = json.load(l)

for loc in locs.keys():
    print(loc)