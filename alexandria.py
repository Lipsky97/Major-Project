import items
import ai_driver
import json

book_found = False
open_canal = False
kitten_found = False
chon_desc = False
curator_met = False
embalming_desc = False
inventory = []
visited = {}
prev_loc = ""
curr_loc = "station"


def play_level(area, unl, itms):
    global book_found
    global open_canal
    global kitten_found
    global chon_desc
    global embalming_desc
    global curator_met
    global inventory
    global visited
    global prev_loc
    global curr_loc
    finished = False
    location = 'alexandria'

    with open('game_files/locations/alexandria.json') as file:
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
            if book_found and curr_loc == "station":
                print(locs[curr_loc]["unlocks"])
            if open_canal and curr_loc == "library":
                print(locs[curr_loc]["unlocks"])
            if kitten_found and curr_loc == "sewers":
                print(locs[curr_loc]["unlocks"])
            if chon_desc and curr_loc == "slums":
                print(locs[curr_loc]["unlocks"])
            if curator_met and curr_loc == "citadel":
                print(locs[curr_loc]["unlocks"])
        else:
            print("You're already here")

        if curr_loc == "sewer" and not kitten_found:
            a = input("Do you want to take the kitten with you?")
            if a == "yes":
                inventory.append("rogers")
                items.pick_up("rogers", location)
            kitten_found = True
            continue

        if curr_loc == "citadel" and not curator_met:
            if ai_driver.chat_bot("curator", location):
                embalming_desc = True
            curator_met = True
            continue

        if curr_loc == "funeral_home":
            finished = True
            with open('game_files/endings/alexandria.json') as file:
                ending = json.load(file)
            if "liquid_moon" in inventory and "embalming_oils" in inventory:
                print(ending["good"])
                break
            elif "liquid_moon" in inventory and "embalming_oils" not in inventory:
                print(ending["semi-good"])
                break
            elif "liquid_moon" not in inventory:
                print(ending["bad"])
                break

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
                # Just people
                if npc == "person" and curr_loc == "cafee":
                    ai_driver.chat_bot("cafee_person", location)
                    continue
                elif npc == "person" and curr_loc == "library":
                    ai_driver.chat_bot("library_person", location)
                    continue
                elif npc == "person" and curr_loc == "slums":
                    ai_driver.chat_bot("slums_person", location)
                    continue
                elif npc == "person" and curr_loc == "aquarium":
                    ai_driver.chat_bot("aquarium_person", location)
                    continue
                elif npc == "librarian":
                    ai_driver.chat_bot("librarian", location)
                    continue

                # Important people
                elif npc == "guy":
                    chon_desc = ai_driver.chat_bot("library_crazy_guy", location)
                    continue
                elif npc == "chon" and chon_desc:
                    if ai_driver.chat_bot("chonsu", location):
                        inventory.append("liquid_moon")
                        print(items.pick_up("liquid_moon", location))
                        continue
                    continue
                elif npc == "baroness" and embalming_desc:
                    if ai_driver.chat_bot("baroness", location):
                        inventory.append("embalming_oils")
                        print(items.pick_up("embalming_oils", location))
                        continue
                    continue
                elif npc == "lamplighter":
                    embalming_desc = ai_driver.chat_bot("lamplighter", location)
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
                if item == "book":
                    book_found = True
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
    global book_found
    global open_canal
    global kitten_found
    global chon_desc
    global embalming_desc
    global curator_met

    if "book_found" in unl:
        book_found = True
    if "open_canal" in unl:
        open_canal = True
    if "kitten_found" in unl:
        kitten_found = True
    if "chon_desc" in unl:
        chon_desc = True
    if "embalming_desc" in unl:
        embalming_desc = True
    if "curator_met" in unl:
        chon_desc = True


def prepare_save():
    global book_found
    global open_canal
    global kitten_found
    global chon_desc
    global embalming_desc
    global curator_met
    global curr_loc
    global inventory

    unl = []
    if book_found:
        unl.append("book_found")
    if open_canal:
        unl.append("open_canal")
    if kitten_found:
        unl.append("kitten_found")
    if chon_desc:
        unl.append("chon_desc")
    if embalming_desc:
        unl.append("embalming_desc")
    if curator_met:
        unl.append("curator_met")

    return curr_loc, unl, inventory
