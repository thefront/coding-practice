#!/usr/local/bin/python3
# NAME: Richard Tzeng
# FILE: lab3.2.cgi
# DATE: <2014-07-14 Mon>
# DESC: This script reads a set of files, prints the name, text source, number 
# of characters, lines, words in the file. It also print the avg num of words
# per sentece, number of paragraphs in each file.  10 most meaning ful words
# in each speed (defined as the number of times each word appears).

print("Content-type: text/html\n")

# Import glob for reading directories, re for regular expressions, and os 
# manipulating path names
import glob
import re
import os

# Read file names, assuming speeches are in public_html/speeches
speeches = glob.glob("../../speeches/*.txt")

# TITLE #
print('<h1>CS 131A Lab3.2.cgi</h1>')

# Process each speech
for speech in sorted(speeches):
    # Open the speech for reading as utf-8 (Unicode)
    s = open(speech, encoding="utf-8")

    # Get all of the lines for the speech
    lines = s.readlines()
    
    # Get just the name of the file, not including the path information
    speech_name = os.path.basename(speech)

    # print out the file name and link to the file 
    print("<h2><a href='/~rtzeng/speeches/{0}'>{1}</a></h2>".format(speech_name,
    speech_name.upper()))

    # print out the table headers
    print('<table border="1" style="width:300px;background:#E8E8E8">')
    print("<tr><th>Chars</th><th>Lines</th><th>Words</th><th>Sentences</th>" +
        "<th>Words@Sent</th><th>Paragraphs</th></tr>")

    # get the total number of characters using os.path.getsize
    print("<tr><td>{}</td>".format(os.path.getsize(speech)))

    # get total lines by len of line list
    print("<td>{}</td>".format(len(lines)))
    
    # Turn the list of lines into a single string. Make all lowercase.
    all_string = "\n".join(lines).lower()

    # turn string into list of words
    all_words = re.split('\W+',all_string)

    # remove empty characters and print
    all_words = [ x for x in all_words if x != '']
    print("<td>{}</td>".format(len(all_words)))

    # Get count of sentences by finding all word and '.' or '?' or '!'
    all_sent = re.split(r'[\.|?|!]', all_string)
    # remove last element and print
    all_sent.pop()
    print("<td>{}</td>".format(len(all_sent)))

    # Average words per sentence is words divided by num sentences
    avg = len(all_words) // len(all_sent)
    print("<td>{}</td>".format(avg))

    # Number of paragraphs counts the occurences of \n\n
    # create one string again
    para_string = "".join(lines)

    # split long string into list at \n\n break
    list_para = re.split(r'\n\n', para_string)

    # remove empty characters and print
    list_para = [ x for x in list_para if x != '']
    print("<td>{}</td><tr>".format(len(list_para)))

    print("</table>")

    """ Start the Ten Most Common Words """
    print("<br><table>")
    print("<tr><td>Ten Most Common Words</td></tr>")

    # Use a list comprehension to get the stop words into a list. Remove
    # the newline from each word.
    stop_words = [i.strip() for i in open('../../stop_words.txt').readlines()]

    # create empty dictionary
    count_words = {}

    # loop to count meaningful words
    for word in all_words:
        if word not in stop_words:
            if count_words.get(word):
                count_words[word] += 1
            else:
                count_words[word] = 1

    # define a custom function for sorting on 2nd value of tuple
    def sort_by_value(x):
        return x[1]

    # sort the word count by items method, using custom function
    sorted_words_tup = sorted(count_words.items(), key=sort_by_value)

    # convert tuple to list and reverse the order
    top_ten = list(sorted_words_tup)
    top_ten.reverse()

    # print the results
    print("<tr><td>{}</td><tr>".format(top_ten[:10]))
    print("</table><hr/>")

### Signature
print('<h3>By Richard Tzeng</h3>')
