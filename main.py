#____Import_Lines_________________________________________________________________


import random

from prisonerid import PrisonerID

from datetime import datetime

from prisoner_generator import crime_generator, name_generator, random_date, race_generator, races

#___Main_Functions________________________________________________________________
def random_4_digit_number():
    return random.randint(1000, 9999)

def valid_date(date):
    try:
        datetime.strptime(date, "%m/%d/%Y")
        return True
    except ValueError:
        return False

#____Customs______________________________________________________________________

def is_integer(x):
    return isinstance(x, int)

def is_natural_number(x):
    return is_integer(x) and x >= 0

def number_in_inclusive_range(number, initial, final):
    if number <= final and number >= initial:
        return True
    else:
        return False

#____Prompts______________________________________________________________________

def terminal_calendar_date_prompt():
    while True:
        birthday = input()
        if valid_date(birthday):
            return birthday
        if birthday == "":
            return ""
        else:
            print("Error: please enter date in month/day/year format: ", end="")

def terminal_whole_number_input_prompt(
    min_value=-(2**63),
    max_value=2**63 - 1,
):
    if not isinstance(min_value, int):
        raise TypeError("min_value must be an integer")

    if not isinstance(max_value, int):
        raise TypeError("max_value must be an integer")

    if min_value > max_value:
        raise ValueError("min_value cannot be greater than max_value")

    while True:
        try:
            number = int(input())
            if min_value <= number <= max_value:
                return number
        except ValueError:
            pass

        print(
            f"Error: enter a whole number from {min_value} to {max_value}: ",
            end="",
        )
        
def terminal_string_input_of_size_prompt(size):
    while True:
        s = input()
        if len(s) <= size:
            return s
        print("Error: input is too long(", size ,") characters max: ", end="")   

def terminal_prompt_natural_number_range(low, high):
    number = 0
    while True:
        while True:
            try:
                number = int(input())
                if is_natural_number(number):
                    break
            except ValueError:
                pass
                
            print("Error: enter a natural number: ", end="")
    
        if number_in_inclusive_range(number, low, high):
            return number
        else:
            print("Error: number is out of range of", low, "to", high, ", try again: ", end = "")
         

def terminal_menu_prompt(options):
    if not options:
        raise ValueError("options cannot be empty")

    print("-" * 40)
    for index, option in enumerate(options, start=1):
        print(f"  [{index}]  {option}")

    print("-" * 40)
    print("Select an option: ", end="")

    selection = terminal_whole_number_input_prompt(
        min_value=1,
        max_value=len(options),
    )

    print()

    return options[selection - 1]    


#____PROGRAM_BELOW___________________________________________________________________

current_date = "June 12th, 1987"
main_character = PrisonerID()

print("Enter prisoner First Name: ", end="")
first_name = terminal_string_input_of_size_prompt(12)
if first_name == "":
    first_name = name_generator()
main_character.first_name = first_name

print("Enter Prisoner Last Name: ", end="")
last_name = terminal_string_input_of_size_prompt(12)
if last_name == "":
    last_name = name_generator()

main_character.last_name = last_name

print("Enter Prisoner birthday: ", end="")
birthday = terminal_calendar_date_prompt()
if birthday == "":
    birthday = random_date("1/1/1900", "6/12/1969")
main_character.birthday = birthday

print("Enter a string to select race:", end ="")
response = input()
if response != "":
    print("_RACE_ENTRY_")
    main_character.race = terminal_menu_prompt(races)
else:
    main_character.race = race_generator()

main_character.prisoner_number = random_4_digit_number()
main_character.crimes.append(crime_generator())

main_character.print_info()




