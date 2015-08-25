#!/usr/local/bin/python3
# NAME: Richard Tzeng
# FILE: lab2.1.cgi
# DATE: <21014-07-04 Tue>
# DESC: Reads oliver.txt file and forms 2 lists of 100 word each.
# The first list will contain the first 100 words. The second list will
# contain the 100 words that start at index 500. Next manipulate the
# strings to print out various unique word sets.

print("Content-type: text/html\n")

import re, string, os, cgi

# Read file into variable
file_string = open('/users/dputnam/public_html/oliver.txt', 'r').read()

# Manipulate string into list of words and assign to a variable. Words are 
# a sequence of alphabetical characters that are separated by non-word
# characters. Use regex to split the string into words and removing newlines.
# A single character is considered a word. Convert to lower case as well. 
lower_words = file_string.lower()
string_to_words = re.split('\W+',lower_words)

# Remove empty elements that are at start or end of string
string_to_words = [x for x in string_to_words if x != '' ]

### 2.1.1 Break into 2 strings
# Break in first 100 words and 500-600
first_hundred = string_to_words[:100]
second_hundred = string_to_words[500:600]

### 2.1.2 For loop to print first 100 words in rows of 6 words
# use length of max element in the list + 2 as character column width
column_width = len(max(first_hundred, key=len)) + 2
count = 0
results = ''

# loop through the first 100 words and break into rows and columns
for x in first_hundred:
    # create columns
    if count == 0:
        results += "{0:>{1}s}".format(str(x), column_width)
    # create new row after count = 6
    elif count % 6 == 0:
        results += '\n'
        results += "{0:>{1}s}".format(str(x), column_width)
    else:
        results += "{0:>{1}s}".format(str(x), column_width)
    # add 1 to count
    count += 1

# print output into HTML format for 2.1.2
print('<H1>Lab2.1.cgi</H1>')
print('<p>2.1.2 Rows with 6 words, columns %s chars (longest word + 2)</p>' % column_width)
print('<table style="background:lightblue;border:solid 2px #888">')
print('<tr><td><pre>')
print(results.rstrip())
print('</pre></td></tr>')
print('</table><hr/>')

### 2.1.3, 2.1.4 count of unique words in first and second 100 words
# use set to create a unique list from the first and second 100 words
first_unique = set(first_hundred)
first_count = len(first_unique)
second_unique = set(second_hundred)
second_count = len(second_unique)

print("<p>2.1.3 The first set of 100 words has %s unique words. They are:</p>" % first_count)
print('<table style="background:lightblue;border:solid 2px #888">')
print('<tr><td>', first_unique, '</td></tr></table><hr/>')
print("<p>2.1.4 The second set of 100 words has %s unique words. They are:</p>" % second_count)
print('<table style="background:lightblue;border:solid 2px #888">')
print('<tr><td>', second_unique, '</td></tr></table><hr/>')

### 2.1.5, 2.1.6 Union of the list and Symmetric Difference
# use format specifiers '|' and '^' to get UNION and symetric difference
union_both = first_unique | second_unique
union_count = len(union_both)
sym_diff = first_unique ^ second_unique
sym_count = len(sym_diff)

print("<p>2.1.5 The two sets combined (UNION) have %s unique words. They are:</p>" % union_count)
print('<table style="background:lightblue;border:solid 2px #888">')
print('<tr><td>', union_both, '</td></tr></table><hr/>')
print("<p>2.1.6 There are %s words that are in one or the other but not both. They are:</p>" % sym_count)
print('<table style="background:lightblue;border:solid 2px #888">')
print('<tr><td>', second_unique, '</td></tr></table><hr/>')

### 2.1.7, 2.1.8 Print the unique words in one set but not in the other
# use an if statement in list comprehension to list out if one word is not in
# the other unique list
in_first = [ x for x in first_unique if x not in second_unique ]
in_first.sort()
in_first_count = len(in_first)
in_second = [ x for x in second_unique if x not in first_unique ]
in_second.sort()
in_second_count = len(in_second)

print("<p>2.1.7 The first set has %s words that are not in the second set. They are :</p>" % in_first_count)
print('<table style="background:lightblue;border:solid 2px #888">')
print('<tr><td>', in_first, '</td></tr></table><hr/>')
print("<p>2.1.8 The second set has %s words that are not in the first set. They are :</p>" % in_second_count)
print('<table style="background:lightblue;border:solid 2px #888">')
print('<tr><td>', in_second, '</td></tr></table><hr/>')

### Signature
print('<h3>By Richard Tzeng</h3>')
