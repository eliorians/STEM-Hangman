from DrT import *
#sets answer to hangman game
word_choices= ["code", "giraffe", "tashakkori"]
difficulty = int(input ("choose a difficulty: 0 for easy, 1 medium, 2 for hard: "))
if difficulty ==0 or difficulty ==1 or difficulty ==2:
    answer= word_choices [difficulty]
else:
    print ("Invalid input, hard choice selected :)") 
    answer= word_choices[2]
#prints a _ for each letter in answer
for i in answer:
    print("_", end=" ")
print("\n")


def main():
    tries = 0
    maxtries=6
    letter_list = []
    while(tries != maxtries):
        guess = input("Guess a letter: ")
        guess= guess.lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in answer:
                print("Nice Job!")
            else:
                tries = tries + 1
                if tries != maxtries:  
                    print("Incorrect, you have used " + str(tries)+ " out of " + str(maxtries)+" tries. ") 
                else:
                    print ("Game Over!") 
        else: 
            print("Invalid input, Try Again :")
       #list of guessed letters
        letter_list.append(guess)
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