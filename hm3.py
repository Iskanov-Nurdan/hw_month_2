class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory


    @property
    def cpu(self):
        return self.__cpu

    @property
    def memory(self):
        return self.__memory

    @property
    def __make_computation(self):
        print(f"Сложение: {self.cpu + self.memory}, Вычитание: {self.cpu - self.memory}")
        print(f"Умноженние: {self.cpu * self.memory}, Деление: {self.cpu / self.memory}")
    @property
    def make_computation(self):
        return self.__make_computation

result = Computer(12,67)
result.make_computation

class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)

        self.__memory_card = memory_card

    def info(self):
        print(f"cpu: {self.cpu}, memory: {self.memory}, memory_card: {self.__memory_card}")

laptop_1 = Laptop(4,765,3456)
laptop_2 = Laptop(98,567,1234)
laptop_3 = Laptop(46,2378,567)

print(laptop_1.cpu)
print(laptop_1.memory)
laptop_1.info()
print(laptop_2.cpu)
print(laptop_2.memory)
laptop_2.info()
print(laptop_3.cpu)
print(laptop_3.memory)
laptop_3.info()


