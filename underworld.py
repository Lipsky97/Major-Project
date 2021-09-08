import items
import json

inventory = []
curr_loc = "underworld_0"


def play_level():

    global curr_loc
    global inventory

    with open('game_files/locations/cracow.json') as file:
        locs = json.load(file)

    while True:
        print(locs[curr_loc]["intro"])
        if curr_loc == "underworld_0":
            answer = input("What do you want to do?\n").lower()

            if "go" in answer:
                words = answer.split()
                loc = words[-1]
                if loc == "field":
                    curr_loc = "underworld_1"
                    continue
                elif loc == "forrest":
                    print("As soon as you come closer to the forrest more spikes appear, "
                          "it doesn't look like the right path")
                    continue
                elif loc == "rift":
                    print("When you lean into the whole you can see a river of "
                          "magma at the bottom. Maybe not this way...")
                    continue
                else:
                    print("Invalid choice")
                    continue

            if "take" in answer:
                inventory.append("clues")
                print(items.pick_up("clues", "cracow"))
                continue

            if "quit" in answer:
                print("Bye!")
                break

        elif curr_loc == "underworld_1":
            answer = input("Type password")
            if answer == "acept":
                curr_loc = "underworld_2"
                continue
            else:
                print("Nothing happened, wrong answer...")
                continue

        elif curr_loc == "underworld_2":
            answer = input("kill/hug?")
            if "kill" in answer:
                print(locs[curr_loc]["unlocks"])

                with open('game_files/endings/cracow.json') as file:
                    ending = json.load(file)

                print(ending["ending"])

                break
            else:
                print("The demon slips out and goes for Lokis neck. Our hero is lying on the floor and bleeding out")
                a = input("Try again?")
                if a in ["y", "yes"]:
                    continue
                else:
                    print("Game Over")
                    break
