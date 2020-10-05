import random

def random_num():
    return random.randint(1, 20)

def formula(a, b):
    return (a*a + b*b) / (a*b)

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
    "belle",
    "kate",
    "michael",
    "tommy",
    "henry"
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
    "boozer",
    "plus8",
    "jozner",
    "kilma",
    "dougles"
]

name = " ".join([random.choice(first), random.choice(last)])
print('random name: ' + str(name))
a = random_num()
b = random_num()
print('random numbers: ' + str(a) + ', ' + str(b))
print('random numbers in formula: ' + str(formula(a, b)))