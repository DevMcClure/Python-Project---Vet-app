from db.run_sql import run_sql

from models.animal import Animal
from models.vet import Vet



def save(vet):
    sql = "INSERT INTO vets (first_name, second_name) VALUES(?,?) RETURNING *"
    values = [vet.first_name, vet.second_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet



def select_all():
    vets = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for row in results:
        vet = Vet(row['first_name'], row['second_name'], row['id'])
        vets.append(vet)
    return vets    



def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0] 

    if result is not None:
        vet = Vet(result['first_name'], result['second_name'], result['id'])
    return vet    


def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM vets WHERE id = ?"
    values = [id]
    run_sql(sql, values)    




def animals(vet):
    animals = []

    sql = "SELECT * FROM animals WHERE vet_id = ?"
    values = [vet.id]
    results = run_sql(sql, values)

    for row in results:
        animal = Animal(row['animal_name'], row['vet_id'], row['date_of_birth'], row['animal_type'], row['owner_contact'], row['treatment_notes'], ['animal_assigned'], ['id'] )
        animals.append(animal)
    return animals    



# in the vet delete, use the animals"vet function" to get all animals for that vet. then update those animals so that their vet = None.
# then delete the Vet    

    