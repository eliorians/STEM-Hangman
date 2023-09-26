from DrT import *

def main():
    tries = 0
    maxtries=6
    letter_list = []

    #select word / game difficulty
    word_choices= ["code", "giraffe", "tashakkori"]
    difficulty = int(input ("choose a difficulty: 0 for easy, 1 medium, 2 for hard: "))

    if difficulty ==0 or difficulty ==1 or difficulty ==2:
        answer= word_choices [difficulty]
    else:
        print ("Invalid input, hard choice selected :)") 
        answer= word_choices[2] 

    #show number of characters in word
    for i in answer:
        print("_", end=" ")
    print("\n")

    #main game loop
    while(tries != maxtries):

        #get letter
        guess = input("Guess a letter: ")
        #force to lower to allow capital letter inputs
        guess= guess.lower()

        #check valid inputs
        if guess.isalpha() and len(guess) == 1:

            #correct answers
            if guess in answer:
                print("Nice Job!")
            #incorrect answers
            else:
                tries = tries + 1
                if tries != maxtries:  
                    print("Incorrect, you have used " + str(tries)+ " out of " + str(maxtries)+" tries. ") 
                else:
                    print ("Game Over!") 
        #invalid inputs
        else: 
            print("Invalid input, Try Again:")

        #keep track of guessed letters
        letter_list.append(guess)

        #show location of correct letters
        for i in answer:
            if i in letter_list:
                print (i, end=" ")
            else:
                print("_", end=" ")
        print ("\n")

        #check if the player has guessed all the letters
        if all(item in letter_list for item in answer):
            print("YOU WIN!!!")
            if (difficulty == 2):
                print (drT)
            break #end the game if the player wins
            
if __name__ == "__main__":
    main()