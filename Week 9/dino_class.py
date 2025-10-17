class Dino:
    def __init__(self, name, species, diet, age):
        self.name = name
        self.species = species
        self.diet = diet
        self.age = age

    def roar(self,):
        print(f"{self.name} lets out a mighty ROAR!")
    
    def eat(self, food):
        if food in self.diet:
            print(f"{self.name} happily eats the {food}!")
        else:
            print(f"{self.name} doesn't eat {food}!")
    
    def dino_info(self,):
        print(f"Name: {self.name}, Species: {self.species}, Diet: {self.diet}, Age: {self.age}")


dino1= Dino("Rex", "T-Rex", ["Meat",], 12)
dino2 = Dino("Diplomat", "Diplodocus", ["Plants",], 35)
dino3= Dino("Raptor", "Oviraptor", ["Meat", "Plants",], 9)

dino1.roar()
dino2.roar()
dino3.roar()
dino1.eat("Meat")
dino1.eat("Plants")
dino2.eat("Meat")
dino2.eat("Plants")
dino3.eat("Meat")
dino3.eat("Plants")
dino1.dino_info()
dino2.dino_info()
dino3.dino_info()