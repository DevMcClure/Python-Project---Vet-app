import pdb
from models.animal import Animal
from models.vet import Vet


import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository



animal_repository.delete_all()
vet_repository.delete_all()


vet_1 = Vet("Phil", "Mitchell")
vet_repository.save(vet_1)
vet_2 = Vet("Ian", "Beale")
vet_repository.save(vet_2)




animal_1 = Animal("Toffie", vet_1, "07.11.16", "Dog", "06912738109", "Bestest Doggo", True)
animal_repository.save(animal_1)
animal_2 = Animal("Lola", vet_1, "12.10.2020", "Dog", "06958819091", "Little Yapper", True)
animal_repository.save(animal_2)
animal_3 = Animal("Jura", vet_2,  "05.06.18", "Dog", "06997152420", "Big Doge", False)
animal_repository.save(animal_3)


animals=animal_repository.select_all()
for animal in animals:
    # print (animal.__dict__)










pdb.set_trace()