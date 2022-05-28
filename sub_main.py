# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    if(sorted(word) == sorted(anagram)):
        return True
    return False


print(find_anagram("teacher", "cheater"))
string1 = "teacher"
string2 = "cheater"
# [assignment] Add your code here


def find_anagram(word, anagram):
    if(sorted(word) == sorted(anagram)):
        return True
    return False


print(find_anagram("Fool", "food"))
string1 = "fool"
string2 = "food"