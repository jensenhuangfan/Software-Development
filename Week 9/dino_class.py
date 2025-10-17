class Dino:
    def __init__(self, name, species, diet, age):
        self.name = name
        self.species = species
        self.diet = []
        self.age = age

    def roar(self,):
        print(f"{self.name} lets out a mighty ROAR!")
    
    def eat(self,):
        pass


dino1= Dino("Rex", "T-Rex", ["Meat"], 12)
dino2 = Dino("Diplomat", "Diplodocus", ["Plants"], 35)
dino3= Dino("Raptor", "Oviraptor", ["Meat", "Plants"], 9)

dino1.roar()
dino2.roar()
dino3.roar()