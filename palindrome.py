#!/usr/bin/env python
# palindrome
import re

pals = [
'''Dennis, Nell, Edna, Leon, Nedra, Anita, Rolf, Nora, Alice, Carol,
Leo, Jane, Reed, Dena, Dale, Basil, Rae, Penny, Lana, Dave, Denny,
Lena, Ida, Bernadette, Ben, Ray, Lila, Nina, Jo, Ira, Mara, Sara,
Mario, Jan, Ina, Lily, Arne, Bette, Dan, Reba, Diane, Lynn, Ed,
Eva, Dana, Lynne, Pearl, Isabel, Ada, Ned, Dee, Rena, Joel,
Lora, Cecil, Aaron, Flora, Tina, Arden, Noel, and Ellen sinned.''',
'',
'''Depardieu, go razz a rogue I draped. ''',
'''Desserts I stressed. ''',
'''Detartrated.''',
'''Devo met a Mr., eh, DNA and her mate moved.''',
'''Di as dad said. ''',
'''Did I draw Della too tall, Edward? I did? ''',
'''Dior droid. ''',
'''DNA-land. ''',
'''Do geese see god? ''',
'''Do good? I? No. Evil anon I deliver. I maim nine more hero-men in Saginaw,
sanitary sword a-tuck, Carol, I. Lo! Rack, cut a drowsy rat in Aswan.
I gas nine more hero-men in Miami. Reviled, I (Nona) live on. I do, O God. ''',
'''"Do nine men interpret?"" "Nine men," I nod. ''']


not_pals = [
    #You can create this one.
    '''This is not a palindrome.''',
    '''is not a palindrome'''
]

def palindrome(stri):
    new_str = re.sub('\W','', stri.lower())
    for indx,ch in enumerate(new_str):
        if ch == new_str[len(new_str) - 1 - indx]:
            continue
        else:
            return False
    return True

## using recursion
def first_char(stri):
    return stri[0]

def last_char(stri):
    return stri[-1]

def middle_chars(stri):
    return stri[1:len(stri) - 1]

def isPalindrome(stri):
    new_str = re.sub('\W','', stri.lower())
    # define base case #1
    if len(new_str) == 0 or len(new_str) == 1:
        return True

    # define base case #2
    if first_char(new_str) != last_char(new_str):
        return False

    # use recursion to determine if they are palindromes
    return isPalindrome(middle_chars(new_str))

print "########## Using for loop"
for i in pals:
    if palindrome(i):
        print(i + " is a palindrome.")
    else:
        print (" -- not a palindrome!")

for x in not_pals:
    if palindrome(x):
        print(x + " is a palindrome.")
    else:
        print(" -- not a palindrome!")

print "########### using recursion"
for i in pals:
    if isPalindrome(i):
        print(i + " is a palindrome.")
    else:
        print (" -- not a palindrome!")

for x in not_pals:
    if isPalindrome(x):
        print(x + " is a palindrome.")
    else:
        print(" -- not a palindrome!")
