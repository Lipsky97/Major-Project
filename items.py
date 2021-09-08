import json


def get_name(item_name, location):
    with open('game_files/items/' + location + '.json') as i:
        items = json.load(i)

    return items[item_name]["name"]


def pick_up(item_name, location):
    with open('game_files/items/' + location + '.json') as i:
        items = json.load(i)

    return items[item_name]["on_pick_up"]


def inspect(item_name, location):
    with open('game_files/items/' + location + '.json') as i:
        items = json.load(i)

    return items[item_name]["inspect"]


def get_location(item_name, location):
    with open('game_files/items/' + location + '.json') as i:
        items = json.load(i)

    return items[item_name]["loc"]