
class Manufacturer:
    def __init__(self, identity, location):
        self.__identity = identity
        self.__location = location
    def describe(self):
        print(f"Identity: {self.__identity} - Location: {self.__location}")

class Device(Manufacturer):
    def __init__(self, name, price, identity, location):
        Manufacturer.__init__(self, identity, location)
        self.__name = name
        self.__price = price
    def describe(self):
        print(f"Name: {self.__name} - Price: {self.__price}")
        super().describe()

device1 = Device(name="mouse", price=2.5, identity=9725, location="Vietnam")
device1.describe()