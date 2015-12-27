#!/usr/bin/python



import spur

import re



shell = spur.SshShell(hostname="4.4.5.5", username="oops", password="opspassword")

with shell:

    result1 = shell.run(["uname","-a"])

    result2 = shell.run(["hostname"])

    result3 = shell.run(["cat","/etc/hosts"])



m = re.search('(^\w+)',result1.output)

firstWord = m.group(0)



print "The result of the regular expression is:"

print "the first result is " + m.group(0)

if firstWord == "Linux":

  print "Found Linux"

print "\n\n"

print "Result output from 'hostname' on the remote computer"

print result2.output



print "\n\n"

print "result output from cat /etc/hosts on remote computer"

print result3.output
