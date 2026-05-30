import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN} Welcome to Sentiment Spy! {Style.RESET_ALL}")

user_name = input(f"{Fore.MAGNETA} Please enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Mystery Agent"

conversation_history = []

print(f"\n{Fore.CYAN} Hello {user_name} !")

print(f"Print a sentence and I will analyse your sentence with TextBlob and show you the sentiment.")

print(f"Type {Fore.YELLOW}reset{Fore.CYAN},{Fore.YELLOW}history{Fore.CYAN}"
      f"or {Fore.YELLOW}exit{Fore.CYAN} to quit.{Style.RESET_ALL}")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter soem text or a valid command.{Style.RESET_ALL}")
        continue
    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE} Exiting Sentiment Spy. Farewell {user_name}! {Style.RESET_ALL}")
        break
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN} All conversation history cleared! {Style.RESET_ALL}")
        continue
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW} No conversation history yet. {Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} No conversation history yet. {Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history,
                                                                    start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😡"
                else:
                    color = Fore.YELLOW
                    emoji = "😭"
                print(f"{idx}"). {color}{emoji} {text} "
                f"Polarity: {polarity:2f}, {sentiment_type}{Style.RESET_ALL}")