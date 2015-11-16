#!/usr/local/bin/ruby
# Author: Richard Tzeng
# Modification Date:  09/15/2014
# SCRIPT: lab2.cgi 
# URL: http://hills.ccsf.edu/~rtzeng/cs132a/lab2.cgi

puts "Content-type: text/html"
puts 

require "open-uri"
require 'cgi'

# grab the string and assing to variable
the_string = ''
open('http://localhost/~dputnam/the_string.cgi') do |f|
  f.each_line { |line| the_string += line }
end

# set some variables for html header and footer
head_html = File.read('head.html')
foot_html = File.read('foot_lab2.html')

header_html = '<h1><code>Lab2.cgi Ruby Arrays</code></h1>'
header_html += '<p>Richard Tzeng -- CS 132A</p>'

# put the string into an array
stgArray = []
the_string.each_line do |x|
  x.each_char do |y|
    stgArray.push(y)
  end
end

# separate into 2 arrays
partOne = Array.new(stgArray[0, stgArray.count/3])
partTwo = Array.new(stgArray[stgArray.count/3, stgArray.count])

# Part 1 and 2
# start the html content of the page and display orig string, 1, and 2
content = "<p>Initial String Array<br><br>#{stgArray}</p>
<pre style='white-space: pre-wrap;word-wrap: break-word'>
<ol>
<li>Print contents of part One.<br><br>#{partOne}</li><br>
<li>Print contents of part two.<br><br>#{partTwo}</li><br>"

# Part 3
# code to intersect the two arrays for part 3
inter = Array.new(partOne & partTwo)

# append to the content 
content += "<li>Print elements common to both One and Two, no duplicates.<br><br>#{inter}</li><br>"

# Part 4
# code to get diff between arrays 1 and 2
diff12 = Array.new(partOne - partTwo)

# append to the content
content += "<li>Print difference between Part One and Part Two.<br><br>#{diff12}</li><br>"

# Part 5
# code to get diff between arrays 2 and 1
diff21 = Array.new(partTwo - partOne)

# append to the content 
content += "<li>Print difference between Part Two and Part One.<br><br>#{diff21}</li><br>"

# Part 6
# Get the last element of part One and Two using at method and display
content += "<li>Print elements at end of Part One and Part Two.<br>
One:<br>#{partOne.at(-1).inspect}<br>
Two:<br>#{partTwo.at(-1).inspect}</li><br>"

# Part 7
# Get the front elements of part One and two using at method and display 
content += "<li>Print elements at front of Part One and Part Two.<br>
One:<br>#{partOne.at(0).inspect}<br>
Two:<br>#{partTwo.at(0).inspect}</li><br>"

# Part 8
# code to delete whitespace, convert to upper case, and insert into
# index 100 of part One
partTwo.delete(" ")
upcaseTwo = partTwo.map(&:upcase)

# creates new array for rest of lab
newTwo = partOne.insert(100, upcaseTwo)

# add to content
content += "<li>Converts part Two into all uppercase. Removes all white space
characters from the array.  Insert new part Two into part One at index
100 to compose a single array.<br><br>#{newTwo}</li><br>"

# Part 9
# code to flatten and remove all white space from new array
flatTwo = Array.new(newTwo.flatten)
flatTwo.delete(" ")

# append to content
content += "<li>Flatten and remove all white space from the new array.<br><br>#{flatTwo}</li><br>"

# Part 10
# code to add '!' to each element of the flattened array
collectTwo = flatTwo.collect {|x| x + '!'}

# append to content
content += "<li>Use Array#collect, add a '!' to each element of the flattened array.<br>
#{collectTwo}</li><br>"

# Part 11
# code to pop the last element and print remainder of array
popTwo = collectTwo.pop

# append to content
content += "<li>Pop the last element and print what's left of the array.<br>
#{popTwo.inspect}<br><br>This is the remaining array:<br><br>#{collectTwo}</li><br>"

# Part 12
# code to insert popped element into index 0
newestTwo = collectTwo.insert(0, popTwo)

# append to content
content += "<li>Insert the popped element into index 0.<br><br>#{newestTwo}</li><br>"

# Part 13
# code to use Array#select to select all uppercase letters with '!'
finalArray = newestTwo.select {|v| v =~ /[A-Z]!/}

# append to content
content += "<li>Finally using Array#select all uppercase letters with '!'<br><br>
#{finalArray}</li></ol></pre>"

# Fill templates with string
html = head_html % [:title => 'Lab2.cgi Ruby Arrays',:banner => header_html,:content => content]

# Print footer
print html + foot_html

# EOF
