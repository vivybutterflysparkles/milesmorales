class clothes:
    def __init__(self, type,size,color,gender):
        self.type = type
        self.size = size
        self.color = color
        self.gender = gender

    def wash(self):
        print(self.type,"is being washed")

cloth1 = clothes("shirt","S","white","Male")
cloth2 = clothes("blouse","XL","blue","Female")
cloth3 = clothes("short","M","red","Male")
cloth4 = clothes("vest","XXL","orange","Female")

print(cloth1.type)
print(cloth1.size)