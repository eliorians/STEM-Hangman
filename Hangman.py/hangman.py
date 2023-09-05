answer = "nutrition"
guess = input("Choose a letter: ")

if guess.isalpha():
    if guess in answer:
        print("Nice Job!")
    else:
        print("incorrect")
else: 
    print("Invalid input, Try Again :")



