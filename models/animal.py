class Animal:

    def __init__(self, animal_name, vet, date_of_birth, animal_type, owner_contact, treatment_notes, animal_assigned = False, id = None):
        self.animal_name = animal_name
        self.vet = vet
        self.date_of_birth = date_of_birth
        self.animal_type = animal_type
        self.owner_contact = owner_contact
        self.treatment_notes = treatment_notes
        self.animal_assigned = animal_assigned
        self.id = id
