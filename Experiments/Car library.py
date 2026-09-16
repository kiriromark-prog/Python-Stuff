class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


    def get_car_info(self):
        return f"Your car is a {self.year} {self.make} {self.model}."

car1 = Car("Ferrrari", "Laferrari" , 2015)    
car2 = Car("Mclaren", "P1" , 2014)
car3 = Car("Porsche", "918 Spyder" , 2013)
car4 = Car("Bugatti", "Chiron" , 2016)
car5 = Car("Lamborghini", "Aventador" , 2017)
car6 = Car("Koenigsegg", "Agera RS" , 2017)
car7 = Car("Pagani", "Huayra" , 2012)
car8 = Car("Aston Martin", "Vulcan" , 2016)
car9 = Car("McLaren", "Senna" , 2018)
car10 = Car("Ferrari", "Enzo" , 2002)


print(car7.get_car_info())