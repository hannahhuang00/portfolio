import time
print('Welcome to Cat & Mouse.')
time.sleep(3)
while True:
    print('You wake up one morning and you feel very odd. You look at your hands and realize they are paws. You say "Oh my gosh!" but it comes out as squeaks. You realize that you turned into a mouse!')
    time.sleep(3)
    print("You exit your mouse hole. Do you go left or right?")
    mouseDirection = input()
    if mouseDirection == "left":
        while mouseDirection == "left":
            print("You decide to go left and you see a delicious piece of cheese. Will you take it, or leave it?")
            cheeseChoice = input()# finished the story by writing what happens
            if cheeseChoice == "take":
                mouseDirection = 0
                print("Oh no! It turns out the cheese was on a mouse trap! Game over.")
            elif cheeseChoice == "leave":
                mouseDirection = 0
                while cheeseChoice == "leave":
                    print("You left the cheese behind and continued safely.")
                    print("You come to two staircases, one going up and one going down. Do you go up or down?")
                    upOrDown = input()
                    if upOrDown == "down":
                        cheeseChoice = 0
                        print("You went down the stairs into the basement and got stuck down there. Game over.")
                    elif upOrDown == "up":
                        cheeseChoice = 0
                        print("You went upstairs, found the pantry, ate all the food and live happily ever after. :D")
                    else:
                        print('This is an invalid option, please choose "up" or "down."')
            else:
                print('That is an invalid option, please choose "leave" or "take."')
    elif mouseDirection == "right":
        while mouseDirection == "right":
            print("You choose to go right and you run into the cat! Will you run or sneak?") # finished the story writing what happens
            catChoice = input()
            if catChoice == "run":
                mouseDirection = 0
                print("The cat noticed you and caught you. Game over.")
            elif catChoice == "sneak":
                mouseDirection = 0
                while catChoice == "sneak":
                    print("Phew, you got away safely.")
                    print("You come to two staircases, one going up and one going down. Do you go up or down?")
                    upOrDown = input()
                    if upOrDown == "down":
                        catChoice = 0
                        print("You went down the stairs into the basement and got stuck down there. Game over.")
                    elif upOrDown == "up":
                        catChoice = 0
                        print("You went upstairs, found the pantry, ate all the food and live happily ever after. :D")
                    else:
                        print('This is an invalid option, please choose "up" or "down."')
            else:
                print('That is an invalid option, please choose "run" or "sneak')
    else:
        print('That is an invalid option, please choose "left" or "right"')
    time.sleep(2)
    print('Type anything to play again and "e" to exit.')
    userAnswer = input()
    if userAnswer == "e":
        print('Goodbye.')
        break
