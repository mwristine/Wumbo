import random

first = [
    "joe",
    "steve",
    "john",
    "adam",
    "alex",
    "andrea",
    "amy"
    "sarah",
    "sam",
    "smitty",
    "sydney"
]

last = [
    "jones",
    "smith",
    "johanson",
    "abner",
    "abbey",
    "aber",
    "solo",
    "sanders",
    "sinker",
    "sawdust"
]

name = " ".join([random.choice(first), random.choice(last)])
print(name)