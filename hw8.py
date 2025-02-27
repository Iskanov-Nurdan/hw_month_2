import sqlite3

connect = sqlite3.connect("bank.db")
cursor = connect.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS customs (
               id INTEGER PRIMARY KEY,
               name VARCHAR (100) NOT NULL,
               surname VARCHAR (100) NOT NULL,
               age INTEDER NOT NULL ,
               email TEXT NOT NULL,
               balance DOUBLE (10, 2) DEFAULT 0.0,
               props VARGHAR (100) NOT NULL,
               is_active BOOLEAN DEFAUL FALSE

);""")

class Bank:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = 0
        self.email = None
        self.balance = 0
        self.props = None
        self.is_active = False
    

    def registr(self, name, surname, age, email):
        self.name = name
        self.surname = surname
        self.age = age 
        self.email = email
        cursor.execute(f"""INSERT INTO customs (name, surname, age, email, balance, props, is_active)
                       VALUES ('{name}','{surname}','{age}','{email}', 0, 0, True);""")
        connect.commit()


    def deposit(self, amount):
        cursor.execute(f""" UPDATE customs SET balance = balance + {amount} WHERE email = '{self.email}'""")
        connect.commit()
        self.balance += amount
    
    def minus(self, amount):
        cursor.execute(f""" UPDATE customs SET balance = balance - {amount} WHERE email = '{self.email}'""")
        connect.commit()
        if amount > self.balance:
            print('извините но вы бомж!')
        else:
            self.balance -= amount
            print(f'вы вывели {amount}, ваш баланс {self.balance}')

    def __str__(self):
        return f"Ваш текущий баланс: {self.balance}"

    def main(self):
        while True:
            print("1 - Регистрация, 2 - Пополнение, 3-Вывести деньги,4- проверка баланса, 5 - выйти ")
            command = int(input("Выберите действие: "))
            if command ==1: 
                print("ЗАРЕГАЙТЕС")
                name = input("Введите ваше имя: ")
                surname = input("введите вашу фамилию: ")
                age = int(input("Введите ваш возраст: "))
                email = input("Введите вашу почту: ")
                print("Регистрация прошла")
                self.registr(name,surname, age, email)
            elif command == 2:
                if self.email:
                    print("ПОПОЛНИТЕ")
                    amount = int(input("Введите сумму: "))
                    self.deposit(amount)
                else:
                    print("СДЕЛАЙТЕ РЕГИСТРАЦИЮ ")
            elif command == 3:
                if self.email:
                    print("ВЫВЕСТИ СРЕДСТВА")
                    amount = int(input("Введите сумму: "))
                    if amount > self.balance:
                        print('извините  вы бомж')
                        break
                    else:
                        self.minus(amount)
            elif command ==4:
                print(self.balance)
                
                        
            elif command == 5:
                break
            else:
                print("1 - Регистрация, 2 - Пополнение, 3-Вывести деньги ,4 - проверка баланса, 5 - выйти ")
                command = int(input("Выберите действие: "))


bank = Bank()
bank.main()
     
   