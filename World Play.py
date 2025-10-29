from random import randint

animals = [["Salmon","Pollock","Cod"],
             ["Parrot","Duck","Wren"],
             ["Camel","Lion","Tiger"]]

random_category = choice(animals)
random_animal = choice(random_category)

if random_animal in animals[0]:
    animal_type = "fish"
elif random_animal in animals[1]:
    animal_type = "bird"
else:
    animal_type = "mammal"

print(f"The randomly selected animal is a {random_animal}, which is a {animal_type}.")