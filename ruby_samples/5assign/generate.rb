#!/usr/local/bin/ruby
# Name: Richard Tzeng
# File: generate.rb
# Desc: create a directory structure and files for a simple web application.
#
# begin
=begin 
*generate.rb*
Creator: Richard Tzeng

This script create a directory structure and provides
some default files that we can use to create a working
CGI-style in a few minutes.

=Templates
This script uses some generic templates to create missing
files. 
=end

# require fileutils --- lots of handy directory and file functions we can use.
require 'fileutils'
include FileUtils
require 'find'

# Usage message
# We run this script on the command line with the
# user providing the name of a directory
# Everything after __END__ is avalable in the DATA hash.

# DIRECTORY             FILE
# ---------             ----
__END__
/                       index.cgi README
app/
app/views/
app/views/layouts/
app/models/
app/controllers/
config/
db/
lib/                    cgi_helper.rb
public/             
public/javascripts/ 
public/stylesheets/ 
public/images/      
log/

Dir.mkdir("")

