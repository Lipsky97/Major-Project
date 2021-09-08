import openai
import json

api_key = ""


def chat_bot(npc_name, location):
    # Start sequences, the chat bot is programmed with the "prompt", that is extended with each sentence, this is
    # specific to the transformer architecture, instead of sending queries one by one each human/AI response is
    # appended to give the AI context for the next answer

    with open('game_files/characters/' + location + '.json') as chars:
        characters = json.load(chars)

    openai.api_key = api_key

    start_sequence = characters[npc_name]["start_seq"]
    restart_sequence = "\nTraveller: "
    prompt = characters[npc_name]["desc"]

    print(characters[npc_name]["first_lines"][0])
    print(characters[npc_name]["first_lines"][1])

    # To create a sense of having a continuous conversation new parts of the prompt are appened in a loop
    while True:
        player_input = input("Traveller: ")
        if player_input != "":
            player_input = player_input
        else:
            print("You didn't say anything, say something")
            continue

        if characters[npc_name]["triggers"][0] in player_input.lower():
            print(characters[npc_name]["finishers"][0])
            return True
        if characters[npc_name]["triggers"][1] in player_input.lower():
            print(characters[npc_name]["finishers"][1])
            return False

        prompt += "Traveller: " + player_input + start_sequence

        response = openai.Completion.create(
          engine="davinci",
          prompt=prompt,
          temperature=characters[npc_name]["ai_vars"]["temp"],
          max_tokens=characters[npc_name]["ai_vars"]["max_tok"],
          top_p=characters[npc_name]["ai_vars"]["top_p"],
          frequency_penalty=characters[npc_name]["ai_vars"]["freq_pen"],
          presence_penalty=characters[npc_name]["ai_vars"]["pres_pen"],
          stop=characters[npc_name]["ai_vars"]["stop"]
        )
        choices = response["choices"]
        choices = choices[0]
        text = choices["text"]

        if text != "":
            print(start_sequence + text)
            if characters[npc_name]["triggers"][0] in text.lower():
                print(characters[npc_name]["finishers"][0])
                return True
            prompt += text + "\n"
        else:
            print("I have no answer to that")
