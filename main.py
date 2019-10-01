import random

first = [
    "joe",
    "steve",
    "john",
    "adam",
    "alex",
    "andrea",
    "amy",
    "jane",
    "amy",
    "sarah",
    "sam",
    "smitty",
    "sydney",
    "cameron",
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
    "jawannaman",
    "solo",
    "sanders",
    "sinker",
    "sawdust",
    "diaz",
    "beck",
    "bender",
    "boxer",
    "boozer"
]

name = " ".join([random.choice(first), random.choice(last)])
print(name)