import openai

api_key = ""

def first_encounter():
    # Start sequences, the chat bot is programmed with the "prompt", that is extended with each sentence, this is
    # specific to the transformer architecture, instead of sending queries one by one each human/AI response is
    # appended to give the AI context for the next answer

    openai.api_key = api_key

    start_sequence = "\nAngel:"
    restart_sequence = "\nTraveller: "
    prompt = "Traveller is sitting in a bar sipping his beer and minding his business. Suddenly a shiny, handsome figure" \
             "is walks into the bar. It is an Angel and his plan is to persuade the Traveller to kill Bacchus. It " \
             "will not be easy as the Traveller is also known as Loki, the god of lies. However, Angel is hoping to" \
             "persuade the traveller with reward Loki can not resist - angel feathers that can make him all powerful." \
             "To seal the deal angel have to make the traveller say 'I accept' phrase and to reject the deal the traveller" \
             "must say 'I reject'" \
             "Here is how the conversation went:\n\n" \
             "Traveller: Who are you?\n" \
             "Angel: I am an Angel, but I think you already know that.\n\n"

    print("Traveller: Who are you?")
    print("Angel: I am an Angel, but I think you already know that.")

    # To create a sense of having a continuous conversation new parts of the prompt are appened in a loop
    while True:
        player_input = input("Traveller: ")
        if player_input != "":
            player_input = player_input
        else:
            print("You didn't say anything, say something")
            continue

        if "I accept" in player_input:
            print("Great, he is hiding in plain sight in small village called Staiti on the south of Italy")
            print("Demo finished, more to come!")
            break
        if "I reject" in player_input:
            print("Angel leaves the traveller to his pint and disappears, nothing has changed, like he never was there")
            print("Game Over")
            break

        prompt += "Traveller: " + player_input + start_sequence

        response = openai.Completion.create(
          engine="davinci",
          prompt=prompt,
          temperature=0.5,
          max_tokens=150,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0.5,
          stop=["\n", " Traveller:", " Angel:"]
        )
        choices = response["choices"]
        choices = choices[0]
        text = choices["text"]

        prompt += text + "\n"


        if text != "":
            # print(text[1:])
            print(start_sequence + text)
        else:
            print("I have no answer for that")