import re,random
from colorama import Fore,init
init(autoreset=True)
destinations = {

"beaches": ["Bali", "Maldives", "Phuket"],

"mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],

"cities": ["Tokyo", "Paris", "New York"]

}

jokes = [

"Why don't programmers like nature? Too many bugs!",

"Why did the computer go to the doctor? Because it had a virus!",

"Why do travelers always feel warm? Because of all their hot spots!"]
def normalize_input(text):
    return re.sub(r"\s+"," ",text.strip().lower())
def recommend():
    print(Fore.CYAN+"TravelBot:beaches,mountains,or cities?")
    prefrence=input(Fore.YELLOW+"You: ")
    prefrence=normalize_input(prefrence)
    if prefrence in destinations:
        suggestions=random.choice(destinations[prefrence])
        print(Fore.GREEN+f"TravelBot:How about {suggestions}?")
        print(Fore.CYAN+"Travelbot: Do you like it?(yes/no)")
        answer=input(Fore.YELLOW+"You:").lower()
        if answer=="yes":
            print(Fore.GREEN+f"TravelBot:Awesome! Enjoy{suggestions}")
        elif answer=="no":
            print(Fore.RED+"TravelBot: Let's try another. ")
            recommend()
        else:
            print(Fore.RED+"TravellBot: I'll suggest again.")
            recommend()
    else:
        print(Fore.RED+"TravelBot: sorry,I don't have that type of destination")
        recommend()
def packing_tips():
    print(Fore.CYAN+"TravelBot:where to?")
    location=normalize_input(input(Fore.YELLOW+"You:"))
    print(Fore.CYAN+"TravelBot:How many days?")
    days=input(Fore.YELLOW+"You:")
    print(Fore.GREEN+f"TravelBot:packing tips for{days}days in{location}:")
    print(Fore.GREEN+"-Pack versatile clothes.")
    print(Fore.GREEN+"-Bring Chargers/adapters.")
    print(Fore.GREEN+"-check the weather forecast")
def tell_joke():
    print(Fore.YELLOW+f"TravelBot:{random.choice(jokes)}")
def show_help():
    print(Fore.MAGENTA+"\n I can:")
    print(Fore.GREEN+"-suggest travel spots(say'recommendation')")
    print(Fore.GREEN+"-offer packing tips(say'packing')")
    print(Fore.GREEN+"-Tell a joke(say'joke')")
    print(Fore.CYAN+"Type 'exit' or 'bye'to end!")
def chat():

    print(Fore.CYAN + "Hello! I'm TravelBot.")

    name = input(Fore.YELLOW + "Your name? ")

    print(Fore.GREEN + f"Nice to meet you, {name}!")

    show_help()

    while True:

        user_input = input(Fore.YELLOW + f"{name}: ")

        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:

            recommend()

        elif "pack" in user_input or "packing" in user_input:

            packing_tips()

        elif "joke" in user_input or "funny" in user_input:

            tell_joke()

        elif "help" in user_input:

            show_help()

        elif "exit" in user_input or "bye" in user_input:

            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")

            break

        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")

if __name__ == "__main__":
    chat()
    