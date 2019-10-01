import random

first = [
    "joe",
    "steve",
    "john",
    "adam",
    "alex",
    "andrea",
    "amy"
]

last = [
    "jones",
    "smith",
    "johanson",
    "abner",
    "abbey",
    "aber"
]

name = " ".join([random.choice(first), random.choice(last)])
print(name)