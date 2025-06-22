import random
friends = ["Arianna", "Jorge", "Jen", "Izio", "Tatis", "Moya", "Gallito"]

random_person = random.choice(friends)
print(random_person)

#opcion 2
print(random.choice(friends))

#opcion 3
random_index = random.randint(0,6)
print(friends[random_index])

