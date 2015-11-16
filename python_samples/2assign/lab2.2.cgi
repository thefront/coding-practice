#!/usr/local/bin/python3
# NAME: Richard Tzeng
# FILE: lab2.2.cgi
# DATE: <21014-07-04 Tue>
# DESC: This script prints out the first 50 Fibonacci numbers.  It shows
# the sequence in four forms:  decimal, hex, octal, and float point number.

print("Content-type: text/html\n")

# defines function to create the Fibonacci numbers
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

#
print('<h1>Lab2.3.cgi</h1>')
print('<h2>Introducing the First 50 Numbers of the Fibonacci Sequence</h2>')

# start the table header
print('<table border="1" style="width:300px;background:#E8E8E8">')
print('<thead><tr><th></th><th>DEC</th><th>HEX</th><th>OCT</th>\
    <th>FLOAT</th><tr></thead>')

# loop through the first four types to print each cell.  The float required
# 2 decimal places so it is separate
for x in range(50):
    # list for first four elements. The first column starts with 1 so the
    # first element needs to be incremented by 1 
    num_seq = (x+1, fib(x), hex(fib(x)), oct(fib(x)))

    print("<tr>")

    # loop the first four columns as they contain repeatable formats
    for row in num_seq:
        print("<td><pre>{0:>20}</pre></td>".format(row))

    # the float format requires 2 decimal places so I separated it out
    print("<td><pre>{0:>20.2f}</pre></td>".format(float(fib(x))))

    print("</tr>")
 
print('</table>')

### Signature
print('<hr/><h3>By Richard Tzeng</h3>')
