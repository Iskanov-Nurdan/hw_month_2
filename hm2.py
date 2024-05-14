class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    def introduce_myself(self):
      print(f"Имя - {self.fullname}, Возраст - {self.age}, Женат/Замужем - {self.is_married}")
inptroduce = Person("Нурдан", 15, "Нет")
inptroduce.introduce_myself()



class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience):
        Person.__init__(self, fullname, age, is_married)
        self.experience = experience
        self.salary = 0   
    
    def info(self):
        print(f"Имя: {self.fullname}, Возраст: {self.age}, Женат/Замужем: {self.is_married}, Опыт работы: {self.experience}")

    def sal(self):
        for i in range(self.experience):
            self.salary += 3000
        print(f"{self.fullname}, Ваша зарплата: {self.salary}")
result = Teacher("Нурдан", 15, "Нет", 4)
result.info()
result.sal()