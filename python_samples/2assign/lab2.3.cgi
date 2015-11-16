#!/usr/local/bin/python3
# NAME: Richard Tzeng
# FILE: lab2.3.cgi
# DATE: <21014-07-04 Fri>
# DESC: This script prints out the properties of the following Python classes:
# 'list', 'dict', 'tuple', 'str', 'int', 'float'
# The HTML table print how many methods and will have seven columns. 

print("Content-type: text/html\n")

# TITLE #
print('<h1>Lab2.3.cgi</h1>')
print('<p>Printing the properties of Python classes:  ' +
    '<b>list, dict, tuple, str, int,</b> and <b>float</b>.</p>')

# Define the lists and Capitalize the headings
the_classes = [list, dict, tuple, str, int, float]
string_classes = ['list', 'dict', 'tuple', 'str', 'int', 'float']
string_classes = [ x.capitalize() for x in string_classes if x != '']

# Loop through the classes to print the properties
for i in range(6):
    # assign a methods to a list
    meth_list = dir(the_classes[i])

    # print the header
    print('<h1>{}</h2>'.format(string_classes[i]))

    # get count of methods and print 
    print(len(meth_list), 'methods')

    # Format table
    print('<table border="1" style="width:300px;background:#E8E8E8">') 

    # separate methods into one list
    table_data = ['<td>{}</td>'.format(element) for element in meth_list ]

    # create seven columns of data in each row
    rows = [table_data[c:c + 7] for c in range (0, len(table_data), 7) ]

    # create HTML row tags
    for r in rows:
        print('<tr>' + " ".join(r) + '</tr>')

    print('</table>')

### Signature
print('<hr/><h3>By Richard Tzeng</h3>')
