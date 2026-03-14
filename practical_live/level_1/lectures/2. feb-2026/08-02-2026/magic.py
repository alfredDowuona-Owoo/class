# class Dog:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

#     def bark(self):
#         print(f"{self.name} barks Woof!!!!")

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

# my_dog = Dog("Billy", 3)
# print(my_dog)

# class Book:
#     def __init__(self, title, author, pages):
#         self.title=title
#         self.author=author
#         self.pages=pages

#     def __str__(self):
#         return f"'{self.title}' by {self.author} - {self.pages} pages."
    
# book1=Book("Animal Farm", "Nii Nortey", 145)
# print(book1)\

# class Animal:
#     def __init__(self, name):
#         self.name=name

#     def speak(self):
#         print(f"{self.name} makes a sound")

# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} barks!! like a dog")

# class Cat(Animal):
#     def meow(self):
#         print(f"{self.name} meow!! like a kittie")


# dog=Dog("Billy")
# dog.speak()
# dog.bark()
# cat=Cat("Peace")
# cat.speak()
# cat.meow()


class BankAccount:
    def __init__(self, balance):
        self.__balance=balance

    def deposit(self, amount):
        if amount > 0:
        #self.amount=amount
            self.__balance+=amount
            print(f"You Deposited {amount}")
        else:
            print("Your Deposit must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance-= amount
            print(f"You withdrew {amount}")
        else:
            print(f"Invalid amount or insufficient funds")

    def get_balance(self):
        return self.__balance
    
account = BankAccount(10000)
account.deposit(2500)
account.withdraw(7000)
print(f"Current Balance : GHS{account.get_balance()}")

