#http://www.foodnetwork.com/recipes/food-network-kitchen/cold-soba-noodle-salad-with-creamy-sesame-dressing-3363160
#hannah huang
print('RECIPE BOX')
print(' ')
print("Type the number of the recipe you wish to view:")
print("1. Cold Soba Noodle Salad with Creamy Sesame Dressing")
recipeName = input()

#soba noodles
if recipeName == '1':
    #ingrediants
    food = ['sesame seeds', 'corn, shucked', 'vegetable oil', 'fresh lemon juice', 'soy sauce', 'packed light brown sugar',
    'chile-garlic sauce', '2-inch piece ginger, peeled and thinly sliced into half moons', '9.5-ounce package dried buckwheat soba noodles',
    'small sprigs watercress', 'cherry tomatoes, halved', 'avocado, diced', 'English cucumber, halved and thinly sliced into half moons']
    amount = ['1/4 cup', '2 ears', '1/2 cup', '1/4 cup', '1/4 cup', '4 teaspoons', '1 teaspoon', '1', '1', '2 cups', '12', '1', '1/2']

    ingrediants = dict(zip(food, amount))

    #print dict
    for items in range(len(ingrediants)):
        print(amount[items]+' '+food[items])

    #instructions
    instructions = ['1. Bring a large pot of water to a boil.', '2.Spread the sesame seeds in a medium skillet over medium heat, and toast until golden brown, shaking the pan occasionally, 4 to 5 minutes. Let cool, about 10 minutes.',
    '3.Meanwhile, add the corn to the boiling water, and cook for 4 to 5 minutes. Remove the corn to a colander, reserving the boiling water for later use, and run the corn under cold water to cool. Cut the kernels from the cobs; set aside.',
    '4.Transfer the sesame seeds to a blender and grind for 15 seconds. Add the oil, and puree until smooth and emulsified, about 15 seconds. Add the lemon juice, soy sauce, sugar, chile-garlic sauce and ginger, and blend for another 15 seconds.',
    '5. Add the soba noodles to the boiling water, and cook until the noodles no longer have a hard, chalky bite but are still springy, 3 to 4 minutes. Strain the noodles in a colander, and run them under cold water to stop the cooking quickly. When the noodles are completely cool, shake the colander vigorously to remove as much water as possible (if the noodles are too wet, they will dilute the dressing).',
    '6.Divide the noodles among four bowls. Drizzle the dressing over the noodles (use all of the dressing, as the noodles will soak it up). Top with the corn, watercress, tomatoes, avocados and cucumbers. Toss before eating.']

    print(" ")
    print("INSTRUCTIONS")

    for x in range(len(instructions)):
        print(instructions[x])
