import ai_driver as ai

def main():

    ai.api_key = input("Please provide OpenAI API key: ")
    ai.first_encounter()


if __name__=="__main__":
    main()