class GeeksPeople:
    def __init__ (self, name, email, phone):
        self.name = name
        self.email = email
        self.phon = phone
    
    def __str__(self):
        return f"Имя - {self.name}, почта - {self.email}, Номер.тел - {self.phone}"

class Student(GeeksPeople):
    def __init__(self, name, email, phone, student_id, group_where_study):
        GeeksPeople.__init__(self, name, email, phone)
        self.student_id = student_id
        self.group_where_study = group_where_study

    def study(self):
        print(f"Имя - {self.name}, Айди - {self.student_id}, Я в группе - {self.group_where_study}")

class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id, group_where_teach):
        GeeksPeople.__init__(self, name, email, phone)
        self.teacher_id = teacher_id
        self.group_where_teach = group_where_teach

    def teach(self):
        print(f"Имя - {self.name}, Айди - {self.teacher_id}, Моя группа - {self.group_where_teach}")

class Admin(GeeksPeople):
    def __init__(self, name, email, phone, admin_id):
        GeeksPeople.__init__(self, name, email, phone)
        self.admin_id = admin_id
       
    def create_group(self):
        print(f"Имя - {self.name}, Айди - {self.admin_id} и я создаю группы")

class Mentor(Teacher, Student):
    def __init__(self, name, email, phone, student_id, teacher_id, group_where_teach,  group_where_study ):
        Teacher.__init__(self, name, email, phone, teacher_id, group_where_teach)
        Student.__init__(self, name, email, phone, student_id, group_where_study)
    
    def ment(self):
        print(f"Имя - {self.name}, мой Айди - {self.teacher_id}, Айди ученика - {self.student_id}, Я в группе - {self.group_where_study}, Моя группа - {self.group_where_teach}")

student = Student("Нурдан", "isakanovnurdan9@gmail.com", 966504736767, 99, "17-1B")
teacher = Teacher("Сыймык", "syimyk04@gmail.com", 996785678475, 1, "17-1B")
admin = Admin("Kaмола", "camola05@gmail.com", 996123465431, 34)
mentor = Mentor("Элиза", "intpliza@gmail.com", 996543567453, 100, 12, "17-1B","15-2B")

student.study()
teacher.teach()
admin.create_group()
mentor.ment()


    




