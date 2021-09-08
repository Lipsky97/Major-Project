import items
import ai_driver
import underworld
import json

welcome = False
spoke_with_priest = False
attack_happened = False
inventory = []
visited = {}
prev_loc = ""
curr_loc = "wawel"


def play_level(area, unl, itms):
    global welcome
    global spoke_with_priest
    global attack_happened
    global inventory
    global visited
    global prev_loc
    global curr_loc
    finished = False
    location = "cracow"

    with open('game_files/locations/cracow.json') as file:
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
            if welcome and curr_loc == "wawel":
                print(locs[curr_loc]["unlocks"])
            if "sword" in inventory and curr_loc == "cave":
                print(locs[curr_loc]["unlocks"])
            if attack_happened and curr_loc == "jubilat":
                print(locs[curr_loc]["unlocks"])
            if "puzzle" in inventory and curr_loc == "hall":
                print(locs[curr_loc]["unlocks"])
            if "sword" in inventory and curr_loc == "gallery":
                print(locs[curr_loc]["unlocks"])
        else:
            print("You're already here")

        if curr_loc == "wawel" and not welcome:
            while True:
                a = input("use powers/river?")
                if "powers" in a:
                    curr_loc = "jail"
                    break
                elif "river" in a:
                    curr_loc = "jubilat"
                    break
                else:
                    print("Wrong input")
            continue

        if curr_loc == "cave" and "sword" in inventory:
            underworld.play_level()
            finished = True
            break



        answer = input("What do you want to do?\n").lower()

        if curr_loc in ["gdynia", "warsaw", "lodz", "gniezno", "kolobrzeg", "sopot"] and "say" in answer:
            if "zagovory" in answer and curr_loc == "gdynia":
                inventory.append("sword")
                print(items.pick_up("sword", location))
                continue
            else:
                print("That's the right word, but wrong crest")
                continue

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
                # Just people
                if npc == "priest":
                    ai_driver.chat_bot(npc, location)
                    spoke_with_priest = True
                    continue
                elif npc == "guard" and curr_loc == "jail":
                    ai_driver.chat_bot("jail_guard", location)
                    continue
                elif npc in ["guard", "guards"] and curr_loc == "gallery":
                    ai_driver.chat_bot("gallery_guard", location)
                    continue
                elif npc in ["student", "students"]:
                    ai_driver.chat_bot("student", location)
                    continue
                elif npc == "daniel":
                    ai_driver.chat_bot("daniel", location)
                    continue
                # Important people
                elif npc == "angel":
                    result = ai_driver.chat_bot("angel", location)
                    if result:
                        attack_happened = True
                        curr_loc = "wawel"
                        continue
                    else:
                        continue
                elif npc == "professor":
                    result = ai_driver.chat_bot("professor", location)
                    if result:
                        inventory.append("puzzle")
                        print(items.pick_up("puzzle", location))
                        continue
                    else:
                        continue
                elif npc == "damian":
                    result = ai_driver.chat_bot("damian", location)
                    if result:
                        attack_happened = True
                        curr_loc = "wawel"
                        continue
                    else:
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
    global welcome
    global spoke_with_priest
    global attack_happened
    if "welcome" in unl:
        welcome = True
    if "spoke_with_priest" in unl:
        spoke_with_priest = True
    if "attack_happened" in unl:
        attack_happened = True


def prepare_save():
    global welcome
    global spoke_with_priest
    global attack_happened
    global curr_loc
    global inventory

    unl = []
    if welcome:
        unl.append("welcome")
    if spoke_with_priest:
        unl.append("spoke_with_priest")
    if attack_happened:
        unl.append("attack_happened")

    return curr_loc, unl, inventory
