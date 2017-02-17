def count_vowels(mystr):
    num_vowels=0
    vowels = ''
    for char in mystr:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
           vowels=vowels + char
    print(vowels)
    return num_vowels
count = count_vowels("banana")
print(count)
