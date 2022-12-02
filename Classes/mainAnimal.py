from Animais import Animal

# animal01 = Animal('Tutu', 'coelho', 3.5)
# animal01.hunt()
#
# animal02 = Animal('Quito', 'ave', 0.12)
# animal02.hunt()
#
# my_animal = Animal()
name_animal = input("Pet's name:\n")
species_animal = input("Pet's species:\n")
weight_animal = int(input("Pet's weight:\n"))
animal1 = Animal(name = name_animal, species= species_animal, weight= weight_animal)
# my_animal.name = name_animal
# my_animal.species = species_animal
# my_animal.weight = weight_animal
# my_animal.hunt()
animal1.hunt()
animal1.define_genere()
print(animal1.genere)