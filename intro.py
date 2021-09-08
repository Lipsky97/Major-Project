import json
import ai_driver


def play_intro():
    with open('game_files/encounters/intro.json') as file:
        description = json.load(file)

    print(description["desc"])
    print(description["desc2"])

    return ai_driver.chat_bot('angel_intro', 'intro')
