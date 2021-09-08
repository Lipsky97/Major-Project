import json

import ai_driver as ai

import staiti
import alexandria
import cracow

import intro
import second_encounter
import third_encounter
import last_encounter


def play_game(level, area, unlocks, items):
    if level == "intro":
        outcome = intro.play_intro()
        if outcome:
            return "staiti", "", [], []
        else:
            return "end", "", [], []
    elif level == "staiti":
        finished, ar, unl, itms = staiti.play_level(area, unlocks, items)
        if finished:
            return "second_encounter", "", [], []
        else:
            return "staiti", ar, unl, itms
    elif level == "second_encounter":
        outcome = second_encounter.play_level()
        if outcome:
            return "alexandria", "", [], []
        else:
            return "second_encounter", "", [], []
    elif level == "alexandria":
        finished, ar, unl, itms = alexandria.play_level(area, unlocks, items)
        if finished:
            return "third_encounter", "", [], []
        else:
            return "alexandria", ar, unl, itms
    elif level == "third_encounter":
        outcome = third_encounter.play_level()
        if outcome:
            return "cracow", "", [], []
        else:
            return "third_encounter", "", [], []
    elif level == "cracow":
        finished, ar, unl, itms = cracow.play_level(area, unlocks, items)
        if finished:
            return "last_encounter", "", [], []
        else:
            return "cracow", ar, unl, itms
    elif level == "last_encounter":
        last_encounter.play_level()
        return "end", "", [], []
    else:
        print("\n\nERROR: LEVEL DOES NOT EXIST '" + level + "'\n\n")


def load_save():
    with open('game_files/saved_games/save.json') as file:
        save = json.load(file)
    lvl = save['level']
    area = save['area']
    unl = save['unlocks']
    itms = save['items']

    return lvl, area, unl, itms


def save_game(lvl, area, unl, itms):
    save = {
        "level": lvl,
        "area": area,
        "unlocks": unl,
        "items": itms
    }

    with open('game_files/saved_games/save.json') as file:
        json.dump(save, file)


def exit_game(lvl, area, unl, itms):
    save_game(lvl, area, unl, itms)
    input("Game saved, press Enter to quit...\n")
    quit(0)


def choose_level():
    answer = input("1. Staiti\n"
                   "2. Alexandria\n"
                   "3. Cracow\n")
    return answer


def how_to_play():
    with open('game_files/how_to_play.json') as file:
        ins = json.load(file)
    print(ins["how_to_play"])


def main_menu():
    answer = input("Angels may Die\n\nWelcome to the game, type:\n\n"
                   "1. How To Play\n"
                   "2. New Game\n"
                   "3. Continue\n"
                   "4. Choose Level\n"
                   "5. Exit Game\n")
    return answer


def main():
    level = "intro"
    area = ""
    unlocks = []
    items = []
    key = ""

    while key == "":
        key = input("Please provide OpenAI API key: ")
        if key == "":
            print("The key is necessary for the game to work!\n")
    ai.api_key = key

    while 1:
        answer = main_menu()

        if answer == "1":
            how_to_play()
        elif answer == "2":
            level, area, unlocks, items = play_game(level, area, unlocks, items)
        elif answer == "3":
            level, area, unlocks, items = load_save()
            level, area, unlocks, items = play_game(level, area, unlocks, items)
        elif answer == "4":
            lvl = choose_level()
            if lvl == "1":
                level = "staiti"
            elif lvl == "2":
                level = "alexandria"
            elif lvl == "3":
                level = "cracow"
            if lvl != "":
                level, area, unlocks, items = play_game(level, "", [], [])
        elif answer == "5":
            exit_game(level, area, unlocks, items)


if __name__ == "__main__":
    main()
