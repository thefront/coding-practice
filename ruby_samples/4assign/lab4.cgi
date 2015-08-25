#!/usr/local/bin/ruby
# author: Richard Tzeng
# date:  10/12/2014
# description:  students /etc/passwd info
#

puts "Content-type: text/html"
puts

# Timing the script
t = Time.now
start = t.to_f

require "open-uri"
require 'cgi'
#require 'erb'
#require 'cgi_helper'

class Student
  @@count = 0
  attr_accessor :user_name, :password, :uid, :gid, :gcos_field, :home_directory, :shell

  def initialize
    if defined?(@@count)
      @@count += 1
    else
      @@count = 1
    end
  end

  def self.count
    @@count
  end

  def webout
    "<tr><td>#{user_name}</td><td>#{password}</td><td>#{uid}</td><td>#{gid}</td>\
    <td>#{gcos_field}</td><td>#{home_directory}</td><td>#{shell}</td></tr>"
  end 
end

# set some variables for html header and footer
head_html = File.read('head_lab4.html')
foot_html = File.read('foot_lab4.html')

header_html = "<h1><code>The /etc/passwd for our class.<br>Richard Tzeng -- CS 132A Lab4.cgi</code></h1>"
content = ""
content += "<table border=\"1\" style=\"width:300px; background:\#E8E8E8\">"
content += "<tr><th>User Name</th><th>Password</th><th>UID</th><th>GID</th>"
content += "<th>GCOS Field</th><th>Home Dir</th><th>Shell</th></tr>"


# read the /etc/group
group_lines = File.readlines("/etc/group")
pass_lines = File.readlines("/etc/passwd")
CRN = 74686

our_class = group_lines.select {|v| v =~ /c74686/}
line_list = our_class.to_s.scan(/\w+/)
users_list = line_list[3..(line_list.length - 2)]
chk = users_list.join("|")
#etc_pass = []
#users_list.each do |name|
#  etc_pass += pass_lines.select { |i| i =~ /#{name}/ }
#end


etc_pass = pass_lines.select {|i| i =~ /#{chk}/}

0.upto(etc_pass.length - 1) do |line|
  entry = Array.new(etc_pass[line].gsub("\n", '').split(/:/))
  stud = "$s" + "#{line}"
  stud = Student.new
  stud.user_name = entry[0]
  stud.password = entry[1]
  stud.uid = entry[2]
  stud.gid = entry[3]
  stud.gcos_field = entry[4]
  stud.home_directory = entry[5]
  stud.shell = entry[6]
  content += stud.webout
end

#puts s0.uid
content +="</table>"

# Time at end of script
finish = Time.now
print 'Elapsed time: ' + (finish.to_f - start.to_f).to_s + "\n"

# Fill templates with string
html = head_html % [:title => 'Lab4.cgi Text Analyzer',:banner => header_html,:content => content]

# Print footer
print html + foot_html
# EOF
