
#sets answer to hangman game
answer = "test"
#prints a _ for each letter in answer
for i in answer:
    print("_", end=" ")
print("\n")
answer = "test"

def main():
    tries = 0
    letter_list = []
    while(tries <= 5):
        guess = input("Choose a letter: ")

        if guess.isalpha():
            if guess in answer:
                print("Nice Job!")
            else:
                tries = tries + 1
                print("incorrect")
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
            break #end the game if the player wins
    print("GAME OVER!",
          "Play Again!")

            
   


if __name__ == "__main__":
    main()