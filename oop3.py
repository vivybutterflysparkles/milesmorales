class devices:
    def __init__(self,model,yom):
        self.model = model
        self.yom = yom
    def crush(self):
        print(self.model,"has crushed")

computer = devices("hp",2008)
computer.crush()

laptop = devices("dell",1992)
laptop.crush()
