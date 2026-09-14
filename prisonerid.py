#____PrisonerID_________________________________________________
class PrisonerID:
    def __init__(self):
        self.prisoner_number = "unknown"
        self.first_name = "unknown"
        self.last_name = "unknown"
        self.address = "unknown"
        self.birthday = "unknown"
        self.race = "unknown"
        self.skin_color = "unknown"
        self.eye_color = "unknown"
        self.height = "unknown"
        self.crimes = []


    def print_info(self):
        print(f"Prisoner ID: {self.prisoner_number}")
        print("├── Name: ", end="")
        print(f"{self.first_name} {self.last_name}")
        print("├── Address: ", end="")
        print(self.address)
        print("├── Birthday: ", end="")
        print(self.birthday)
        print("├── Race: ", end="")
        print(self.race)
        print("├── Eye Color: ", end="")
        print(self.eye_color)
        print("├── Height: ", end="")
        print(self.height)
        print("└── Crimes: ", end="")
        print(self.crimes)


