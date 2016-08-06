#!/usr/bin/env ruby
# Author: Richard Tzeng
# Modification Date:  08/05/2014
# SCRIPT: mt.rb

puts "Content-type: text/html"
puts

require 'cgi'
require 'net/ssh'

Net::SSH.start("localhost", "rtzeng") do |ssh|
  # 'ssh' is an instance of Net::SSH::Connection::Session
  output  = ssh.exec!("hostname")
  output2 = ssh.exec!("uptime")
  puts output
  puts output2
end

# set some variables for html header and footer
head_html = File.read('head.html')
foot_html = File.read('foot.html')

header_html = '<h1><code>Lab2.cgi Ruby Arrays</code></h1>'
header_html += '<p>Richard Tzeng -- CS 132A</p>'


# define content
content = "
<p>
  Initial String Array<br><br>
  #{output}
</p>
<pre style='white-space: pre-wrap;word-wrap: break-word'>
"
content += output2

# Fill templates with string
html = head_html % [
  :title => 'Lab2.cgi Ruby Arrays',
  :banner => header_html,
  :content => content
]

# Print footer
print html + foot_html

# EOF
