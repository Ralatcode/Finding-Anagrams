# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

try:
        word = str(input("Enter the first word: "))
        anagram = str(input("Enter the second word: "))
except:
        print("Error, this is not a string!!")

def find_anagram(word, anagram):
    # [assignment] Add your code here
 
    if len(word) == len(anagram):
        if sorted(word) == sorted(anagram):
            return print(True)
        else:
            return print(False)
    else:
        print("This words are not the same length and cant be an anagram")

find_anagram(word, anagram)

# note: this function only tests for words that are anagrams
# it will return not the same length, if we compare word sentence that are anagrams
