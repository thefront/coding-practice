#!/usr/bin/env ruby
# this is a practice program from java class
# writing this in ruby for practice
# description: prompt user for number of astericks to print out, print them,
#              then ask user to repeat or not
#
# inputs: number and where to repeat or not
# outputs: number of astericks

# assign variable whether to repeat to yes
repeat = "y"

# continous loop to print for number of astericks and then print, and ask to
# play again
while repeat != "n"
  print "How many astericks to print? "
  num = gets.rstrip

  puts "*" * num.to_i

  print "Do you want to play again? [y/n]: "
  repeat = gets.rstrip
end
