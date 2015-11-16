#!/usr/local/bin/ruby
# 
# Add the current directory to the include path.
$:.unshift('.')  
require 'cgi_helper'
require 'cgi'
include CGI_Helper

# print the Content-type line
http_header

number = CGI.params['number'][0].to_i

# Normally print a number, but if number is 0 (zero) 
# we expect a ZeroDivisionError exception which will kill our script.
# We can handle this possibility with an exception
begin 
  # If number is > 0, no problem.
  puts 9 / number 
rescue ZeroDivisionError => e
  puts "Division by zero is not permitted."
  print e.message + '<br />'
  puts e.backtrace.join('<br />')
end
