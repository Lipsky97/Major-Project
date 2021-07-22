import json

with open('game_files/items/staiti.json') as i:
    items = json.load(i)


def get_name(item_name):
    return items[item_name]["name"]


def pick_up(item_name):
    return items[item_name]["on_pick_up"]


def inspect(item_name):
    return items[item_name]["inspect"]


def get_location(item_name):
    return items[item_name]["loc"]