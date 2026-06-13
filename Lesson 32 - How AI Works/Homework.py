import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}Welcome to Sentiment Spy!{Style.RESET_ALL}")

user_name = input(
    f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}"
).strip()

if not user_name:
    user_name = "Mystery Agent"

conversation_history = []

print(f"\n{Fore.CYAN}Hello {user_name}!{Style.RESET_ALL}")
print("Type a sentence and I will analyze its sentiment.")
print(
    f"Type {Fore.YELLOW}history{Fore.CYAN}, "
    f"{Fore.YELLOW}stats{Fore.CYAN}, "
    f"{Fore.YELLOW}reset{Fore.CYAN}, or "
    f"{Fore.YELLOW}exit{Fore.CYAN}.{Style.RESET_ALL}"
)

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    if user_input.lower() == "exit":

        positive = sum(
            1 for _, _, sentiment in conversation_history
            if sentiment == "Positive"
        )
        negative = sum(
            1 for _, _, sentiment in conversation_history
            if sentiment == "Negative"
        )
        neutral = sum(
            1 for _, _, sentiment in conversation_history
            if sentiment == "Neutral"
        )

        total = len(conversation_history)

        print(f"\nTotal Messages: {total}")
        print(f"{Fore.GREEN}Positive: {positive}{Style.RESET_ALL}")
        print(f"{Fore.RED}Negative: {negative}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Neutral: {neutral}{Style.RESET_ALL}")

        print(
            f"\n{Fore.BLUE}Exiting Sentiment Spy. Farewell {user_name}!{Style.RESET_ALL}"
        )
        break

    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}All conversation history cleared!{Style.RESET_ALL}")
        continue

    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            for idx, (text, polarity, sentiment_type) in enumerate(
                conversation_history, start=1
            ):

                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😡"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"

                print(
                    f"{idx}. {color}{emoji} {text} "
                    f"(Polarity: {polarity:.2f}, {sentiment_type})"
                    f"{Style.RESET_ALL}"
                )

        continue

    elif user_input.lower() == "stats":

        positive = sum(
            1 for _, _, sentiment in conversation_history
            if sentiment == "Positive"
        )
        negative = sum(
            1 for _, _, sentiment in conversation_history
            if sentiment == "Negative"
        )
        neutral = sum(
            1 for _, _, sentiment in conversation_history
            if sentiment == "Neutral"
        )

        total = len(conversation_history)

        print(f"Total Messages: {total}")
        print(f"{Fore.GREEN}Positive: {positive}{Style.RESET_ALL}")
        print(f"{Fore.RED}Negative: {negative}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Neutral: {neutral}{Style.RESET_ALL}")

        continue

    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < 0:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😡"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    print(
        f"{color}{emoji} Sentiment: {sentiment_type} "
        f"(Polarity: {polarity:.2f}){Style.RESET_ALL}"
    )

    conversation_history.append(
        (user_input, polarity, sentiment_type)
    )