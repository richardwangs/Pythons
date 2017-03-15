import re
filename = 'C:/Users/Senpai/Desktop/Pyhon/Pythons/GoldenAge.txt'
word_dict = {}
filenamehandle = open(filename, 'r')
text_string = filenamehandle.read().lower()
match_pattern = re.findall('\w+', text_string)

for word in match_pattern:
    count = word_dict.get(word,0)
    word_dict[word] = count + 1
     
for word in word_dict:
    print(word + ' : ' + str(word_dict[word]))
