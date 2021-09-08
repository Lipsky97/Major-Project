import json
import ai_driver


def play_level():
    with open('game_files/encounters/last_encounter.json') as file:
        desc = json.load(file)

    print(desc["desc"])
    ai_driver.chat_bot("angel", "last_encounter")
    print(desc["desc2"])
