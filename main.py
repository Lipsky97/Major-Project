import ai_driver as ai
import staiti
import intro


def main():
    ai.api_key = input("Please provide OpenAI API key: ")
    if intro.play_intro() is True:
        staiti.play_level()
    else:
        print("Game Over")

if __name__ == "__main__":
    main()