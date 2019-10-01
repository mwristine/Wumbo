import random

first = [
    "joe",
    "steve",
    "adam",
    "alex",
    "andrea",
    "amy"
]

last = [
    "jones",
    "smith",
    "abner",
    "abbey",
    "aber"
]

name = " ".join([random.choice(first), random.choice(last)])
print(name)