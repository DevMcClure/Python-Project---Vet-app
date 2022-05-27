class Animal:

    def __init__(self, animal_name, date_of_birth, animal_type, owner_contact, treatment_notes, animal_registered = False, id = None):
        self.animal_name = animal_name
        self.date_of_birth = date_of_birth
        self.animal_type = animal_type
        self.owner_contact = owner_contact
        self.treatment_notes = treatment_notes
        self.animal_registered = animal_registered
        self.id = id
