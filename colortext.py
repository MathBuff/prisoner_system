from colorama import Fore, init
init()

color = {
    "red": Fore.RED,
    "yellow": Fore.YELLOW,
    "green": Fore.GREEN,
    "cyan": Fore.CYAN,
    "blue": Fore.BLUE,
    "magenta": Fore.MAGENTA,
    "reset": Fore.RESET
}


#use examples:
def rainbow(text):
    for code in color.values():
        print(code + text + Fore.RESET)

#rainbow("Hello, World!")        

#print(color["red"]+ "I farted " + color["reset"]+ "lmao")

#coloring input after prompt:
#name = input("Enter your name: " + color["cyan"])
#print(color["reset"])



#