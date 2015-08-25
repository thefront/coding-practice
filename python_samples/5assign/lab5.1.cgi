#!/usr/local/bin/python3
# NAME: Richard Tzeng
# FILE: lab5.1.cgi
# DATE: <2014-07-28 Mon>
# DESC: This script creates a base64 encoding string of an image and uses it as
# the background image. Next we print the Unicode characters from 33-126 and 128
# to 3999.

print("Content-type: text/html\n")

# Import other modules
import base64
import cgi

# set up the base64 string image 
bytes1 = base64.b64encode(open('/students/rtzeng/public_html/images/external-link-icon.gif','rb').read()) 
back_image1= str(bytes1)[2:-1].strip()

bytes2 = base64.b64encode(open('/students/rtzeng/public_html/images/plaid.gif','rb').read()) 
back_image2= str(bytes2)[2:-1].strip()

# Print out the HTML style header
print('''<!DOCTYPE html>
<html>
  <head>
    <title>Lab5.1.cgi</title>
      <meta charset="utf-8">
      <style type="text/css">
        body {
          background-color:white;
          background:url(data:image/gif;base64,%s);
          font-family:"Arial Unicode MS", "Arial", "Tahoma";
          font-weight:bold;font-size:30px;color:#c00;text-shadow:0 0 2px black,0px 0px 8px white;
          text-align:center
        }
        #theBox {
          background-color:white;
          background:url(data:image/gif;base64,%s);
          border:solid 2px #555;text-align:center;
          border: 2px solid #00ffff; width:1000px;
          overflow:auto;padding:17px;margin:0 auto; 
        }
        div {
          font-family:Arial;font-size:30px;color:#00ff00;
          text-shadow:none;background-color:#c0c0c0;width:40px;margin:0 auto
        }
        .uni-char {
          background-color:#ff00ff;
          border:solid 2px #444;
          box-shadow: 2px 2px 4px gray;
          min-width:10%%;
          font-size:48px;
          min-height:100px;
          text-align:center;
          float:left;
          margin:8px;
          padding:8px;
          padding-top:24px;
          margin-left:11px;
        }
        sub {
          padding-top:8px;
          display:block;
          clear:both;padding-top:18px;
          font-size:12px;color:#0000ff;
        }
      </style>
    </head>''' % (back_image1, back_image2))

print('''<body>
<h1>CS 131A lab5.1.cgi</h1>
<h2>Arial</h2>
<hr>
Printable Characters that Hurt the Eyes: 33 - 126, 128 - 4000
<hr>
<div id="theBox">''')

# Print out the Unicode for 33 to 126 using for loop
for x in range(33,127):
    print('<div class="uni-char">',end='')
    """ 
    1) Because we're displaying the characters, we need to use HTML entities. The `cgi` 
       module has the necessary functions to do this.
    2) Strings are by default encoded as unicode, so we have to change that
       encoding to `ascii`.
    3) We use the `xmlcharrefreplace` option to convert the characters to 
       xml entities."""

    char = cgi.escape(chr(x)).encode("ascii", "xmlcharrefreplace")
    # When we print the character, we have to decode bytes to characters.
    print(char.decode(),end='')
    print('<div class="clearfix"></div><sub>{}</sub></div>'.format(x))

# do the same for 128 to 3999
for x in range(128,4000):
    print('<div class="uni-char">',end='')
    char = cgi.escape(chr(x)).encode("ascii", "xmlcharrefreplace")
    print(char.decode(),end='')
    print('<div class="clearfix"></div><sub>{}</sub></div>'.format(x))

print("</div>")
print("</body>")
print("</html>")
