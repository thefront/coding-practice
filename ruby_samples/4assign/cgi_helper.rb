#!/usr/local/bin/ruby
# Author:  Richard Tzeng
# date:  10/20/2014
# description: helper file

module CgiHelper 

 def render_file_with_erb(file) 
    rhtml = File.read(file) or raise "Could not open " + file
    render_erb(rhtml)
 end 

 def render_erb(rhtml) 
    require 'erb' 
    erb = ERB.new(rhtml) 
    erb.result(binding) 
 end 

end 

# Test on the command line
if __FILE__ == $0
  include CgiHelper
  puts render_file_with_erb('CgiHelper.rb')
end
