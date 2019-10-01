import random

first = [
    "joe",
    "steve",
    "john",
    "adam",
    "alex",
    "andrea",
    "amy",
    "jane"
]

last = [
    "jones",
    "smith",
    "johanson",
    "abner",
    "abbey",
    "aber",
    "jawannaman"
]

name = " ".join([random.choice(first), random.choice(last)])
print(name)