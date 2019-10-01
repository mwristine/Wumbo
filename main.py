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
    "jawannaman"
    "solo",
    "sanders",
    "sinker",
    "sawdust"
]

name = " ".join([random.choice(first), random.choice(last)])
print(name)