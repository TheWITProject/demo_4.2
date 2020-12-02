from app import db

class Zoo(db.Model):
    __tablename__ = "zoos"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String) # optional: extract to new Address table

    animals = db.relationship("Animal", back_populates="zoo")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }


class Animal(db.Model):
    __tablename__ = "animals"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.Date) 

    zoo_id = db.Column(db.Integer, db.ForeignKey("zoos.id"))
    zoo = db.relationship("Zoo", back_populates="animals")

    species_id = db.Column(db.Integer, db.ForeignKey("species.id"))
    species = db.relationship("Species", back_populates="animals")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birthday": self.birthday,
            "zoo_id": self.zoo_id,
            "species_id": self.species_id
        }


class Species(db.Model):
    __tablename__ = "species"

    id = db.Column(db.Integer, primary_key=True)
    colloquial_name = db.Column(db.String)
    scientific_name = db.Column(db.String)
    sound = db.Column(db.String)

    animals = db.relationship("Animal", back_populates="species")

    def serialize(self):
        return {
            "id": self.id,
            "colloquial_name": self.colloquial_name,
            "scientific_name": self.scientific_name,
            "sound": self.sound
        }