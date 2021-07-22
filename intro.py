import ai_driver

def play_intro():
    print("Loki, the god of lies is sitting at the bar, having a pint minding his business. Life of an immortal is "
          "nice, nobody bothers you, and you come out on top during any fight with mortals, so as long as you're "
          "not messing with other godly entities you're fine. This is what Loki has been doing for centuries now "
          "as most of his family is dead or hiding after the rise of christianity. He escaped using his tricks "
          "as he always does. However this night turned out to be different")

    return ai_driver.chat_bot("angel_intro")
