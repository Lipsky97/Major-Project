import items
import ai_driver
import json

letter = False
drunk = False
inventory = []
visited = {}
prev_loc = ""
curr_loc = "lobby"


def play_level(area, unl, itms):

    global letter
    global inventory
    global visited
    global prev_loc
    global curr_loc
    global drunk
    finished = False
    location = 'staiti'

    with open('game_files/locations/staiti.json') as file:
        locs = json.load(file)

    for locale in locs.keys():
        visited[locale] = False

    load_unlocks(unl)
    inventory = itms
    if area != "":
        curr_loc = area

    while True:
        if curr_loc != prev_loc:
            if visited.get(curr_loc) is False:
                print(locs[curr_loc]["intro"])
                visited[curr_loc] = True
            print(locs[curr_loc]["desc"])
            if letter and locs[curr_loc]["unlocks"] is not None:
                print(locs[curr_loc]["unlocks"])
        else:
            print("You're already here")
        answer = input("What do you want to do?\n").lower()

        if "go" in answer:
            words = answer.split()
            loc = words[-1]
            if loc in locs[curr_loc]["go_to"]:
                prev_loc = curr_loc
                curr_loc = loc
                continue
            else:
                print("Invalid location")
                continue

        if "talk" in answer:
            words = answer.split()
            npc = words[-1]
            if npc in locs[curr_loc]["talk_to"] and locs[curr_loc]["talk_to"] is not None:
                if npc == "drunkard" and letter is False:
                    ai_driver.chat_bot("drunk_guy_0", location)
                    continue
                elif npc == "drunkard" and letter is True:
                    drunk = ai_driver.chat_bot("drunk_guy_1", location)
                    continue
                elif npc == "worker" and letter is False:
                    letter = ai_driver.chat_bot("post_worker", location)
                    inventory.append("letter")
                    print(items.pick_up("letter", location))
                    continue
                elif npc == "worker" and letter is True:
                    print("No much to talk about...")
                    continue
                elif npc == "bartender" and drunk is False:
                    ai_driver.chat_bot("bartender_0", location)
                    continue
                elif npc == "bartender" and drunk is True:
                    result = ai_driver.chat_bot("bartender_1", location)
                    if result is True:
                        finished = True
                        with open('game_files/endings/staiti.json') as e:
                            endings = json.load(e)
                        if 'pistol' in inventory and 'cross' in inventory:
                            print(endings["good"])
                            break
                        elif 'pistol' in inventory:
                            print(endings["semi_good"])
                            break
                        else:
                            print(endings["bad"])
                            break
                    else:
                        continue
                elif npc == "lorenzo":
                    ai_driver.chat_bot("story_teller", location)
                    continue
                elif npc == "lady":
                    ai_driver.chat_bot("old_lady", location)
                    continue
                elif npc == "pedestrian":
                    ai_driver.chat_bot("pedestrian", location)
                    continue
            else:
                print("Invalid NPC")
                continue

        if "take" in answer:
            words = answer.split()
            item = words[-1]
            if item in locs[curr_loc]["items"] and locs[curr_loc]["items"] is not None:
                inventory.append(item)
                print(items.pick_up(item, location))
                continue
            else:
                print("Invalid selection")
                continue

        if "inventory" in answer:
            print(inventory)
            continue

        if answer == "quit":
            print("Bye!")
            break

    return finished, prepare_save()


def load_unlocks(unl):
    global letter
    global drunk
    if "letter" in unl:
        letter = True
    if "drunk" in unl:
        drunk = True


def prepare_save():
    global letter
    global drunk
    global inventory
    global curr_loc

    unl = []
    if letter:
        unl.append("letter")
    if drunk:
        unl.append("drunk")

    return curr_loc, unl, inventory
