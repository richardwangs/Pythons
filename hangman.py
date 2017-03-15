import random
import string
filename = "C:/Users/Senpai/Desktop/Pyhon/Pythons/word_list.txt"
filenamehandle = open(filename, 'r')
line = filenamehandle.readline()
wordlist = line.split()
word = random.choice(wordlist)  
dashes = "-" * len(word)      
wrong = 0                    
usedletters = []                     
print("Hangman is a game where you guess the word with only 6 guesses")

while (wrong < 6) and (dashes != word):
    print ("Incorrect guesses: ", usedletters)
    print ("Word so far:", dashes)
    guess = input("\n\nEnter your guess: ")
    guess = guess.lower()

    while(len(guess)>1) or(guess.isalpha()==False):
        print("Letter only please! ")
        guess = input("Enter your guess: ")
        guess = guess.lower()
    
    while(guess in usedletters):
        print ("You've already guessed the letter:", guess)
        guess = input("Enter your guess: ")
        guess = guess.lower()

    if (guess in word):
        print ("Correct!")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += dashes[i]              
        dashes = new

    else:
        print("Incorrect!")
        wrong += 1
        usedletters.append(guess)
    print("You have used %i of six guesses"%wrong)


if (wrong == 6):
    print("You've been hanged!")
else:
    print("You WIN!")
    
print ("The word was", word)
