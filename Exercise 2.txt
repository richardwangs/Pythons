words_dict= {}
number = 1
def word_dictionary():
    number = int(input('Hello my name is word_dictinary please enter a integer from 1 to 3: '))
    while number != 0: 
        if number == 1:
            if len(words_dict)== 0:
                print("There's no word in the dictionary yet")
            else:
                print(words_dict)
        elif number == 2:
            word = input('enter a word ')
            meaning = input('enter them meaning ')
            if word in words_dict:
                print("do not allow duplicate entries")
            else:
                words_dict[word]= meaning
        elif number ==3:
            lookup = input('what word to look up :')
            if lookup in words_dict:
                print(words_dict[lookup])
                
            else:
                print("Word not found")
        number = int(input('Please enter a integer from 1 to 3: '))
word_dictionary()
