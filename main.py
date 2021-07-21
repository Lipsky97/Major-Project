import ai_driver as ai


def main():
    ai.api_key = input("Please provide OpenAI API key: ")
    ai.chat_bot("angel_intro")


if __name__ == "__main__":
    main()