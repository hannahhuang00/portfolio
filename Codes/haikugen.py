#Hannah Huang
#This code generates a random haiku

import random
fiveSyl = ['I went to the fridge', 'Today will be good', 'Hamburger hotdog', 'Ice cream, ice cream, dog',
'If the sun is green', 'The floor is lava', 'Refrigerator', 'Two plus two is 4',
'Literally dead']
sevenSyl = ['OMG relatable', 'Circles have eleven sides', 'Cherries are usually red', "Potato, tomato, toe", "P V equals n R T"]
print(random.choice(fiveSyl)+",")
print(random.choice(sevenSyl)+",")
print(random.choice(fiveSyl)+".")
