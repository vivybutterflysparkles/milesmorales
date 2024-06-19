class car:
    def __init__(self, model, color,manufacturer, year):
        self.model = model
        self.color = color
        self.manufacturer = manufacturer
        self.year = year

    def speed(self):
        print("the manufacturer of",self.model,"is",self.manufacturer)

car1 = car("B12","blue",'BMW','2021')
car1.speed()
car2 = car("B12","white",'BMW','2021')
car2.speed()
car3 = car("B12","red",'BMW','2021')
car3.speed()
car4 = car("B12","orange",'BMW','2021')
car4.speed()
car5 = car("B12","pink",'BMW','2021')
car5.speed()
car6 = car("B12","yellow",'BMW','2021')
car6.speed()
