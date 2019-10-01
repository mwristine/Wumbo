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
    "sydney",
    "benny",
    "bobert",
    "bonnie",
    "belle"
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
    "sawdust",
    "beck",
    "bender",
    "boxer",
    "boozer"
]

name = " ".join([random.choice(first), random.choice(last)])
print(name)