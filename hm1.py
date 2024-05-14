class Fruits:
    # fruits = 3
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def info(self):
        print(f"Нозвания {self.name}, цвет {self.color} масса {self.weight}")

fruts_1 = Fruits("Яблока", "Красный", "6-5kr")
fruts_2 = Fruits("Мандарин", "Оранживый", "140г")
fruts_3 = Fruits("Банан", "Жолтый", "150г")


fruts_1.info()
fruts_2.info()
fruts_3.info()
print(fruts_1.info)

class Heroes:
    def __init__(self, name, role, health, rasa):
        self.name = name
        self.role = role
        self.health = health
        self.rasa = rasa

    def info(self):
        print(f"Имя:{self.name}, роль:{self.role} здоровье:{self.health} расcа:{self.rasa}")

    def action1(self):
        print(f"{self.name} Сабирает уражай")
    def action2(self):
        print(f"{self.name} Спасает деревню")
    def action3(self):
        print(f"{self.name} Лечит раниных")

        
heroes_1 = Heroes("Jeck", "Farmer", "34xp", "Humen")
heroes_2 = Heroes("Soring", "Hunter", "100xp", "Ogre")
heroes_3 = Heroes("Aisim", "cook", "57xp", "Elf")


heroes_1.info()
print(heroes_1.name)
heroes_2.info()
heroes_3.info()
heroes_1.action1()
heroes_2.action2()
heroes_3.action3()



