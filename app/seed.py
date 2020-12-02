from models import Zoo, Animal, Species
import datetime

def seed(db):
    zoos = [
        Zoo(id=1, name="Bronx Zoo",address="Bronx"),
        Zoo(id=2, name="Central Park Zoo", address="Manhattan")
    ]

    species = [
        Species(id=1, colloquial_name="cow", scientific_name="bos taurus", sound="moo"),
        Species(id=2, colloquial_name="pig", scientific_name="sus scrofa", sound="oink oink"),
        Species(id=3, colloquial_name="dog", scientific_name="canis familiaris", sound="bark")
    ]

    animals = [
        Animal(name="Bessie", birthday=datetime.date(2020, 1, 1), zoo_id=1, species_id=1),
        Animal(name="Betty", birthday=datetime.date(2020, 1, 1), zoo_id=1, species_id=1),
        Animal(name="Stanley", birthday=datetime.date(2020, 1, 1), zoo_id=2, species_id=1),
        Animal(name="Manly", birthday=datetime.date(2020, 1, 1), zoo_id=2, species_id=1),
        Animal(name="Wilbur", birthday=datetime.date(2020, 1, 1), zoo_id=1, species_id=2),
        Animal(name="Wendy", birthday=datetime.date(2020, 1, 1), zoo_id=1, species_id=2),
        Animal(name="Candy", birthday=datetime.date(2020, 1, 1), zoo_id=2, species_id=2),
        Animal(name="Dandy", birthday=datetime.date(2020, 1, 1), zoo_id=2, species_id=2),
        Animal(name="Shiloh", birthday=datetime.date(2020, 1, 1), zoo_id=1, species_id=3),
        Animal(name="Sheepdog", birthday=datetime.date(2020, 1, 1), zoo_id=2, species_id=3)
    ]

    db.session.add_all(zoos)
    db.session.add_all(species)
    db.session.add_all(animals)
    db.session.commit()