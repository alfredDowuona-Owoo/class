#class Car:
    #def __init__(self, brand, model, year):
       # self.brand = brand
       # self.model = model
       #self.year = year

    #def drive(self):
        #print(f"The {self.year}, {self.brand} {self.model} is a driving Car")

    #def stop(self):
        #print(f"The {self.brand} has stopped")


#my_car = Car("Toyota", "Corolla", 2015)
#your_car = Car("Honda", "Civic", 2024) 


#my_car.drive()
#my_car.stop()

class DataScience_CBG:
    def __init__(self, name, role, line_manager, marital_status):
        self.name = name
        self.role = role
        self.line_manager = line_manager
        self.marital_status=marital_status

    def skill(self, programming_language, skill_level):
        self.programming_language = programming_language
        self.skill_level = skill_level
        print(f"{self.name} can code in {self.programming_language} with a skill level of {self.skill_level}")

    def unit(self, unit):
        self.unit=unit
        print(f"{self.name} is a {self.role} and is {self.marital_status}")
        print(f"{self.name} works under the {self.unit} units and reports to {self.line_manager}")

my_people = DataScience_CBG("Elsie", "Data Analyst", "Alfred", "Single")
my_people.skill("Python", 6)
my_people.unit("Data Science")