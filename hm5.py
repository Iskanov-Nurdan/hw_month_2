# class MagicCalcultor:
#     def __init__(self, numbers_1, numbers_2):
#         self.numbers_1 = numbers_1
#         self.numbers_2 = numbers_2

#     def __add__(self, other):
#         result = self.numbers_1 + other.numbers_1
#         return f"Результат сложения: {result}"

    
#     def __sub__(self, other):
#         result = self.numbers_1 - other.numbers_1
#         return f"Результат сложения: {result}"
    
#     def __mul__(self, other):
#         result = self.numbers_1 * other.numbers_1
#         return f"Результат сложения: {result}"

    
#     def __truediv__(self, other):
#         result = self.numbers_1 / other.numbers_1
#         return f"Результат сложения: {result}"


# num1 = MagicCalcultor(10, 10)
# num2 = MagicCalcultor(12, 12)
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)


class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __str__(self):
        return f"Названия книги: {self.name}, Автор книги: {self.author}, год выпуска книги: {self.year}"

    def book(self):
        print(f"Названия книги: {self.name}, Автор книги: {self.author}, год выпуска книги: {self.year}")

    def __gt__(self, other):
        return self.year > other.year

    def __lt__(self, other):
        return self.year < other.year

    def __eq__(self, other):
        return self.year == other.year 

    def __ne__(self, other):
        return self.year != other.year

    def __ge__(self, other):
        return self.year >= other.year

    def __le__(self, other):
        return self.year <= other.year


book1 = Book("Война и мир", "Лев Толстой", 1869)
book2 = Book("Мцыри", "Лермантов", 1840)
book3 = Book("Капита́нская до́чка", "Пушкин", 1836)

book1.book()

book2.book()

book3.book()

print(book1 > book2 > book3)
print(book1 < book2 < book3)
print(book1 == book2 == book3)
print(book1 != book2 != book3)
print(book1 >= book2 >= book3)
print(book1 <= book2 <= book3)