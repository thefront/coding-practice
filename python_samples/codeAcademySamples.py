#! /usr/bin/env python

# Scrabble score
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word):
    total = 0
    for x in word:
        total += score[x.lower()]
    return total

print scrabble_score("zztestthiswWord" )
# end scrabble_ score


# is_prime
def is_prime(n):
    if n < 2:
        return False
    for x in range(2, n - 1):
        if n % x == 0:
            return False
    return True

print is_prime(2)
print is_prime(5)
print is_prime(1)
print is_prime(7)
# end is_prime


# reverse
def rev(st):
    result = []
    for x in range(len(st)):
        result.append(st[len(st) - x - 1])
    return "".join(result)

print rev("wow does thi readlly work")
# end reverse

# anti vowel
def anti_vowel(st):
    res = []
    for c in st:
        if c not in "aeiouAEIOU":
            res.append(c)
    return ''.join(res)

print anti_vowel("Testifthis string is avowle")
# end vowel

# enumerate example
def censor(text, word):
    txtList = text.split()
    for index,item in enumerate(txtList):
        if word == item:
            txtList[index] = "*" * len(item)
    return " ".join(txtList)
# end enumerate

# remove duplicate
def remove_duplicates(nums):
    res = []
    for item in nums:
        if item not in res:
            res.append(item)
    return res
# end duplicate
