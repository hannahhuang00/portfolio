#Hannah Huang
#Randomly generates things to get from a menu
import random
appetizers = ['Cheese and Crackers', 'Chips and Salsa', 'Dumplings'] #appetizer list
entrees = ['Fish Filet', 'Steak', 'Salad'] #entree list
sides = ['Fries', 'Fruits', 'Soup'] #side list
drinks = ['Soda', 'Water', 'Tea', 'Coffee'] #drink list
desserts = ['Ice Cream', 'Cake'] #desset list
print("Appetizer: "+random.choice(appetizers)) #picks random appetizer
print('Entree: '+random.choice(entrees)) #random entree
print('Side: '+random.choice(sides)) #random side
print('Drink: '+random.choice(drinks)) #random drink
print('Dessert: '+random.choice(desserts)) #random dessert
