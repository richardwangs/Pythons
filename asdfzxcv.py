vowels = 'aeiouAEIOU'
lists =[] 
def count_vowels(mystr):
    if not mystr:
        print (lists)
        lists.clear()
        return 0
    elif mystr[0] in vowels:
        lists.append(mystr[0])
        return 1 + count_vowels(mystr[1:])
    else:
        return 0 + count_vowels(mystr[1:])
print (count_vowels("banana"))
print (count_vowels("apple"))

