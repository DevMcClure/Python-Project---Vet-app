PRAGMA FOREIGN_KEYS = ON;

DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS vets;


CREATE TABLE vets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR,
    second_name VARCHAR
);



CREATE TABLE animals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    animal_name VARCHAR,
    date_of_birth VARCHAR,
    animal_type VARCHAR,
    owner_contact VARCHAR,
    treatment_notes VARCHAR,
    animal_assigned BOOLEAN,
    vet_id INTEGER NOT NULL,
        FOREIGN KEY (vet_id)
            REFERENCES vets(id) ON DELETE CASCADE
);