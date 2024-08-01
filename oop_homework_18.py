class Automobile:
    INITIAL_MILEAGE: int = 0

    def __init__(self, manufacturer: str, brand: str, fuel_consumption: float, year_of_issue: int = 2020):
        self.year_of_issue = year_of_issue
        self.manufacturer = manufacturer
        self.brand = brand
        self.mileage = self.INITIAL_MILEAGE
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return f'A {self.brand} car, released in {self.year_of_issue}'


car1 = Automobile('Germany', "BMW", 7.0, 2023)
car2 = Automobile("Italy", 'Lamborghini', 8.3)
car3 = Automobile('Japan', 'Mazda', 9.7, 2012)
