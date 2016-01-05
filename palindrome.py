#!/usr/bin/env python
# palindrome
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
    import re
    new_str = re.sub('\W','', stri.lower())
    for indx,ch in enumerate(new_str):
        if ch == new_str[len(new_str) - 1 - indx]:
            continue
        else:
            return False
    return True


for i in pals:
    print(i)
    if palindrome(i):
        print(i + " is a palindrome.")
    else:
        print (" -- not a palindrome!")

for x in not_pals:
    print(x)
    if palindrome(x):
        print(x + " is a palindrome.")
    else:
        print(" -- not a palindrome!")
