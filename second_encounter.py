import json


def play_level():
    with open('game_files/encounters/secound_encounter.json') as file:
        desc = json.load(file)

    input(desc["desc"])
    input(desc["desc2"])
    input(desc["desc3"])
    while True:
        a = input("Continue? (y/n)")
        if a == "y":
            input(desc["desc4"])
            return True
        elif a == "n":
            return False
        else:
            print("Invalid answer")

