#!/usr/bin/python
# NAME: Richard Tzeng
# FILE: lab6.1.cgi
# DATE: <2014-08-01 Fri>
# DESC: This script will build a database-backed form that allows users to add
# URLs to the database.  This uses Python 2.6.6 on hills.

# Import other modules
#import htmllib
import cgitb
cgitb.enable()
import cgi
import os
import sqlite3
import sys

# defaults
user_name = ''
assignment = ''
url = ''

# use only this password
password = 'summer2014cohort!'
links = []
errors = []

# allowed student list
ccsf_students = "dputnam,smccorm2,jgurung2,wli13,kkrauss,cmyers,eyao,csander6,jsteimni,jlarsen3,aboak,jmencha1,mhawver,jmo6,bparra,mkunze,ckwan17,iburenin,mnicasio,rtzeng,uaddison,whuttner,gwong7,abettini,ahapp,cferrei2,creeve,psakhark,dboone1,npachec2,ftan".split(',')

try:
    if os.environ['REQUEST_METHOD'] == 'POST':
        if ('user_name' in ccsf_students) and ccsf_students["user_name"].value.strip != '':
            user_name = request["user_name"].value
            url = request["url"].value
            assignment = request["assignment"].value
            connect = sqlite3.connect('lab6.1.db')
            cursor = connect.cursor()
            cursor.execute("INSERT INTO student_urls (user_name, assignment, url, created_at) values(?, ?, ?, date('now'))", (user_name,assignment,url))
            connect.commit()
        #print('''Status: 302 Moved Temporarily
       # X-Powered-By: Python 3.3
       # Location: /~rtzeng/cs131a/lab6.1.cgi
       # Content-type: text/html\n''')

       # # It's important to exit!
       # sys.exit()

    else:
        errors.append('Hills username missing')
except Exception as e:
    error_string = e

request = cgi.FieldStorage()

print("Content-type: text/html\n")

print('''<!doctype html>  
<html lang="en-us">  
  <head>  
    <meta charset="utf-8">  
    <title>Lab 6.1: CGI Form</title>  
    <meta name="description" content="Form for entering AppEngine and Herokuapp URLs">  
    <meta name="author" content="Richard Tzeng">  
    <!--[if lt IE 9]>  
    <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>  
    <![endif]-->    
  </head>  
  <body>
    <form action="" method="post">
    <h1>Assignment 6: <small>lab6.1.cgi</small></h1>
    <h3>Info</h3>
        <ul><li>Only <b>appspot.com</b> or <b>herokuapp.com</b> domains allowed.</li>
        <li>Your CCSF UserId must be in the list of students registerd for CS
        131A.</li>
        <li>Use the Password available in the assignment.</li>
        </ul>
    <div id="headline"><h1>Register your Cloud web app</h1></div>
    <p>
      <label for="assignment">Assignment</label>
      <select name="assignment">
        <option value="6">6 CGI Form</option>
        <option value="7">7 Google App Engine</option>
        <option value="8">8 More App Engine</option>
        <option value="9">9 Heroku App Engine</option>
      </select>
    </p>
    <p>
      <label for="user_name">Hills UserID</label>
      <input type="text" name="user_name" value="" id="user_name" required
      placeholder="Your Hill Billy UserName">
    </p>
    <p>
      <label for="url">Cloud URL</label>
      <input type="url" name="url" value="" required placeholder="http://what?"> 
    </p>
    <p>
      Use the password specified in Assignment 6.</p>
    <p>
     <label for="password">Authentication</label>
     <input type="password" name="password" value="" required placeholder="ssshhhhhh"> 
    </p>
    <p style="text-align:center;padding-top:1.4em;margin-bottom:0">
      <input type="submit" name="submit" value="Submit URL">
    </p>
    </form>
'''.format(assignment=cgi.escape(assignment), user_name=cgi.escape(user_name), url=cgi.escape(url), password=cgi.escape(password)))


#if errors:
#    print('<ul><li>','</li></li'.join(errors),'</li></ul>')



#all = cursor.execute("SELECT * FROM student_urls order by created_at, user_name")

    # write the rest of the code
#if user_name:
#    all = cursor.execute("SELECT * FROM student_urls where user_name = ? order by created_at",(user_name,))
#    for row in all:
#        links.append('[{}] {} <a href="{}">{}</a> <div style="float:right">{}</div>'.format(row[2],row[1], row[3],row[3],row[4]))
#else:
#    all = cursor.execute("SELECT * FROM student_urls order by created_at, user_name")
#    for row in all:
#        links.append('[{}] {} <a href="{}">{}</a> <div style="float:right">{}</div>'.format(row[2],row[1], row[3],row[3],row[4]))


print("</body>")
print("</html>")
