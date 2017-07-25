#Hannah Huang
#Random names
import random
boyNames = ['Jerry', 'Bob', 'Henry', 'Phil', 'Corey', 'Dan', 'Jonah', 'Tony']
girlNames = ['Sally', 'Patricia', 'Ella', 'Sarah', 'Clarissa','Nancy', 'Lilly']
print ('Choose "boy" or "girl" name.')
    nameList = input()
    if nameList == "boy":
        print(random.choice(boyNames))
    if nameList == "girl":
        print(random.choice(girlNames))
