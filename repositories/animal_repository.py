from db.run_sql import run_sql

from models.animal import Animal 
from models.vet import Vet
import repositories.vet_repository as vet_repository




def save(animal):
    sql = "INSERT INTO animals (animal_name, vet_id, date_of_birth, animal_type, owner_contact, treatment_notes, animal_assigned) VALUES (?,?,?,?,?,?,?) RETURNING *"
    values = [animal.animal_name, animal.vet.id, animal.date_of_birth, animal.animal_type, animal.owner_contact, animal.treatment_notes, animal.animal_assigned]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal




def select_all():
    animals = []


    sql = "SELECT * FROM animals"
    results= run_sql(sql)

    for row in results:
        animal_assigned = True if row ['animal_assigned'] == 1 else False
        vet = vet_repository.select(row['vet_id'])
        animal = Animal(row['animal_name'], vet, row['date_of_birth'], row['animal_type'], row['owner_contact'], row['treatment_notes'], animal_assigned, row['id'])
        animals.append(animal)
    return animals  


def select(id):
    animal = None 
    sql = "SELECT * FROM animals WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]


    if result is not None:
        vet = vet_repository.select(result['vet_id'])
        animal = Animal(result['animal_name'], vet, result['date_of_birth'], result['animal_type'], result['owner_contact'], result['treatment_notes'], result['id'])
    return animal    
        


def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)   


def delete(id):
    sql = "DELETE  FROM animals WHERE id = ?"
    values = [id]
    run_sql(sql, values)



def update(animal):
    sql = "UPDATE animals SET(animal_name, vet_id, date_of_birth, animal_type, owner_contact, treatment_notes, animal_assigned) = (?, ?, ?, ?, ?, ?, ?) WHERE id = ?"
    values = [animal.animal_name, animal.vet_id, animal.date_of_birth, animal.animal_type, animal.owner_contact, animal.treatment_notes, animal.animal_assigned, animal.id]
    run_sql(sql, values)


