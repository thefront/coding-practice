#!/usr/local/bin/ruby
# Author: Richard Tzeng
# Modification Date: 09/08/2014
# File Name: lab1.rb
# Desc: This script will "sanitize" the string located in 
#       http://hills.ccsf.edu/~dputnam/the_string.cgi
#       It will "normalize" meaning capitalize sentences, set other characters
#       to lower case, remove extra spaces between words.
#
puts "CS 132A"
puts

# Fetch the string from the url
require "open-uri"
the_string = ""
the_url = "http://hills.ccsf.edu/~dputnam/the_string.cgi"

open(the_url) do |content|
  content.each_line { |line| the_string += line }
end

puts "The string we will work with:\n"
puts the_string
puts 

puts "#{'#' * 8} 1 Squeeze"
puts the_string.squeeze(" ")
puts '#' * 8
puts 

puts "#{'#' * 8} 2 downcase"
puts the_string.downcase
puts '#' * 8
puts

puts "#{'#' * 8} 3 upcase"
puts the_string.upcase
puts '#' * 8
puts

puts "#{'#' * 8} 4 Removing the Ending \'X\'"
puts the_string.gsub(/X$/, '')
puts '#' * 8
puts

puts "#{'#' * 8} 5 each_byte"
puts "----------"
puts "C|Dec|Hex "
puts "----------"
puts  [ the_string.each_byte { |c| printf "%c|%3d|0x%x\n", c, c, c } ] - [ the_string ]
puts '#' * 8
puts

puts "#{'#' * 8} 6 split"
puts 'Splitting using the default delimiter (white space). Note that
empty elements are not shown.'
puts
puts the_string.split(/\s+/).inspect
puts
puts 'Splitting with an explicit \s parameter.'
puts
puts the_string.split(/\s/).inspect
puts '#' * 8 
puts

puts "#{'#' * 8} 7 crypt"
print "String: \""
print the_string
puts '"'
print "Encrypted: "
puts the_string.crypt("ABC1231.")
puts '#' * 8
puts

puts "#{'#' * 8} 8 replace"
start_string=the_string[0,100].strip.reverse.squeeze.upcase
end_string=the_string[100,the_string.length]
final_string=start_string,end_string
puts final_string.join('')
puts '#' * 8
puts

puts "#{'#' * 8} 9 inspect"
puts final_string.join('').inspect
puts '#' * 8
puts

puts "#{'#' * 8} 10 Capitalize first alphabetical character of each line"
the_string.each_line do |line|
  first_word = /[a-zA-Z]+/.match(line, 1)
  puts line.sub(/[a-zA-Z]+/, first_word.to_s.capitalize)
end
puts '#' * 8
puts
