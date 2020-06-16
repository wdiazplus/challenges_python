# Restaurant: Make a class called Restaurant . The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type .
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.

class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f'The name is {self.restaurant_name} and your cuisine type is {self.cuisine_type}') 
    
    def open_restaurant(self):
        print(f'{self.restaurant_name} is open')

#Instance
restaurant = Restaurant('Mypizza', 'Italian cuisine')
print(('*')*100)
#Name of instance
print(restaurant.restaurant_name)
print(('*')*100)
#Cuisine type of instance
print(restaurant.cuisine_type)
print(('*')*100)
# Using methods
restaurant.describe_restaurant()
print(('*')*100)
restaurant.open_restaurant()
print(('*')*100)
print(('*')*100)


# Three Restaurants: Start with your class from Exercise previous. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

restaurant_one = Restaurant('Myhambur', 'USA cuisine')
restaurant_two = Restaurant('MyTamal', 'Colombian cuisine')
restaurant_three = Restaurant('Myfish', 'Random cuisine')
restaurant_one.describe_restaurant()
restaurant_two.describe_restaurant()
restaurant_three.describe_restaurant()

print(('*')*100)
print(('*')*100)


# Make a class called User . Create two attributes called first_name
# and last_name , and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

class user :

    def __init__ (self, first_name, last_name, age, gender, client_active ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.client_active = client_active
    
    def describe_user(self):
        print(f'The user is {self.first_name} {self.last_name} with {self.age} old years, is {self.gender} and {self.client_active} client')     
    def greet_user(self):
        print(f'Hola {self.first_name} Welcome our restaurant')


Jaz = user('Jas','McClain', 24, 'male', 'no active')
So = user('Sol','McCarthur', 44, 'female', 'active')
Mi = user('Dara','Miranda', 14, 'female', 'active')
Jo = user('john','Juarez', 64, 'male', 'active')


print(('*')*100)
Jaz.describe_user()
Jaz.greet_user()
print(('*')*100)
So.describe_user()
So.greet_user()
print(('*')*100)
Mi.describe_user()
Mi.greet_user()
print(('*')*100)
Jo.describe_user()
Jo.greet_user()

