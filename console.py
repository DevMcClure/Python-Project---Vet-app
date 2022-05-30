import pdb
from models.animal import Animal
from models.vet import Vet


import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository



animal_repository.delete_all()
vet_repository.delete_all()


vet1 = Vet("Phil", "Mitchell")
vet_repository.save(vet1)
vet2 = Vet("Ian", "Beale")
vet_repository.save(vet2)
vet3 = Vet("Not", "Assigned")
vet_repository.save(vet3)




animal_1 = Animal("Toffie", vet1, "07.11.16", "Dog", "06912738109", "Bestest Doggo", True)
animal_repository.save(animal_1)
animal_2 = Animal("Lola", vet2, "12.10.2020", "Dog", "06958819091", "Little Yapper", True)
animal_repository.save(animal_2)
animal_3 = Animal("Jura", vet3,  "05.06.18", "Dog", "06997152420", "Big Doge", False)
animal_repository.save(animal_3)


animals=animal_repository.select_all()
for animal in animals:
    print (animal.__dict__)


# vets=vet_repository.select_all()
# for vet in vets:
#     print (vet.__dict__)









pdb.set_trace()