sentence = "this is a sample sentence. Hello my name is aditya"
words = sentence.split() #seperating the words from the sentence as individual word

word_occurence={}  #creating an empty dictionary

for word in words:
    # print(word)
    word_occurence[word]=words.count(word)  #countiong the occurence of a word  and storing it to the dictionary
print(word_occurence)    
