import random
from datetime import datetime, timedelta

crimes = [
    "Aggrevated Assault",
    "Domestic Violence",
    "Rape",
    "Murder",
    "Attempted Murder",
    "Child Molestation",
    "Domestic Terrorism",
    "Mass Murder",
    "Human Trafficking",
    "Kiddnapping",
    "Armed Robbery",
    "Public Nudity",
    "Malicious Medical Malpractice",
    "Drug Trafficking",
    "Attempted Genocide"
    ]
    
names = ["Logan",
        "Martin",
        "Eduardo",
        "Jacob",
        "Eugine",
        "Jenkins",
        "John",
        "Aubery",
        "Mullen",
        "Dean",
        "Curtis",
        "Clay",
        "Cummins",
        "Johnny",
        "Ramirez",
        "Gideon",
        "Dixon",
        "Lucas",
        "Brian",
        "Mulligan",
        "Eduardo",
        "Villasenor",
        "Herson",
        "Alexander",
        "Zachary",
        "Snodgrass",
        "Jesus",
        "Castanon",
        "Evan",
        "Owens",
        "Tyler",
        "Keil",
        "Ryan",
        "St. John",
        "Ethen",
        "Siazon",
        ]
        
races = ["Black or African American", 
        "Asian", 
        "American Indian or Alaska Native",
        "Hispanic or Latino",
        "Middle Eastern or North African",
        "Native Hawaiian or Pacific Islander",
        "White"
        ]

def crime_generator():
    return random.choice(crimes)

def name_generator():
    return random.choice(names)

def race_generator():
    return random.choice(races)

    
#Returns a random date between two MM/DD/YYYY dates, inclusive.
def random_date(lower_bound: str, upper_bound: str) -> str:
    fmt = "%m/%d/%Y"

    lower = datetime.strptime(lower_bound, fmt)
    upper = datetime.strptime(upper_bound, fmt)

    if lower > upper:
        raise ValueError("lower_bound must not be later than upper_bound")

    days = (upper - lower).days
    random_offset = random.randint(0, days)

    return (lower + timedelta(days=random_offset)).strftime(fmt)

