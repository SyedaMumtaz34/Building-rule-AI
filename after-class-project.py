import re
from colorama import Fore, Style, init

init(autoreset=True)

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return Fore.GREEN + "Hello! How can I help you?"

    elif re.search(r"\b(bye|goodbye|exit)\b", user_input):
        return Fore.RED + "Goodbye! Have a nice day!"

    elif "how are you" in user_input:
        return Fore.CYAN + "I'm doing great! Thanks for asking."

    else:
        return Fore.YELLOW + "Sorry, I don't understand that yet."


print(Fore.BLUE + " Welcome to My Rule-Based Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    user_input = input(Fore.WHITE + "You: ")

    response = chatbot_response(user_input)
    print("Bot:", response)

    if re.search(r"\b(bye|goodbye|exit)\b", user_input.lower()):
        break