import random

first = [
    "joe",
    "steve",
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