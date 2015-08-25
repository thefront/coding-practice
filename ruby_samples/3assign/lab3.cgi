#!/usr/local/bin/ruby
# Author: Richard Tzeng
# Modification Date:  10/06/2014
# SCRIPT: lab3.cgi 
# URL: http://hills.ccsf.edu/~rtzeng/cs132a/lab3.cgi
# This script will read in speeches from presidents and output statistics.

puts "Content-type: text/html"
puts 

require "open-uri"
require 'cgi'

# set some variables for html header and footer
head_html = File.read('head_lab3.html')
foot_html = File.read('foot_lab3.html')

header_html = "<h1><code>The Ruby Text Analyzer!!!<br>Richard Tzeng -- CS 132A Lab3.cgi</code></h1>"

# Set stop words array
stopwords = File.read("/users/dputnam/public_html/stop_words.txt").split

# start the begin/rescue/end exception block
begin
  # TEXT ANALYZER CODE GOES HERE.
  # In case of an exception, execution will jump to the rescue block
  # where you can handle the exception, or simply display a message.

  # Start empty string for html content
  content = ""

  # read the speeches into a variable and loop through analyzer
  Dir.glob("/students/rtzeng/public_html/speeches/*.txt").each do |file|
    # get the file name, president name
    file_name = file.split(/\//)
    president = file_name[5].upcase.chomp(".TXT").gsub(/_/, ' ')

    # Process lines from the speech file
    lines = File.readlines(file)
    text = lines.join

    # process text to UTF-8 encoding
    processed_text = text.force_encoding('UTF-8').gsub(/\s+/,'')

    # Count lines, characters with and w/o space
    line_count = lines.size
    total_characters = text.length
    total_characters_nospaces = processed_text.gsub(/\s+/, '').length

    # Count the words, sentences, and paragraghs
    word_count = text.split.length
    sentence_count = text.split(/\.|\?|!/).length
    paragragh_count = text.split(/\n\n/).length

    # Make a list of works in the text that aren't stop words,
    # count them, and work out the percentage of non-stop words
    # against all words
    all_words = text.scan(/\w+/)
    all_lower = all_words.map(&:downcase)
    good_words = all_lower.select{ |word| !stopwords.include?(word) }
    good_percentage = ((good_words.length.to_f / all_words.length.to_f) * 100).to_i

    # Summarixe the text by cherry picking some choice sentences
    sentences = text.gsub(/\s+/, ' ').strip.split(/\.|\?|!/)
    sentences_sorted = sentences.sort_by { |sentence| sentence.length }
    one_third = sentences_sorted.length / 3
    ideal_sentences = sentences_sorted.slice(one_third, one_third + 1)
    ideal_sentences = ideal_sentences.select { |sentence| sentence =~ /be|was|have|has|is|are|am/ }
    ideal_sen_out = ideal_sentences[0,7].push("")

    # Find the 10 most common words
    counter = {}
    good_words.each do |t|
      if counter.include?(t)
        counter[t] += 1
      else
        counter[t] = 1
      end
    end 
    top_10 = counter.sort {|a,b| a[1] <=> b[1]}

    # Output the results into HTML
    content += "<h1><a href=\"http://hills.ccsf.edu/~rtzeng/speeches/#{file_name[5]}\" "
    content += "target=\"_blank\"> #{president} Inauguration Speech</a></h1>"
    content += "<h3>STATISTICS</h3>"
    content += "<table border=\"1\" style=\"width:300px; background:\#E8E8E8\">"
    content += "<tr><td>Lines</td><td>#{line_count}</td></tr>"
    content += "<tr><td>Characters</td><td>#{total_characters}</td></tr>"
    content += "<tr><td>Characters (exc. space)</td><td>#{total_characters_nospaces}</td></tr>"
    content += "<tr><td>Word Count</td><td>#{word_count}</td></tr>"
    content += "<tr><td>Sentences</td><td>#{sentence_count}</td></tr>"
    content += "<tr><td>Paragraphs</td><td>#{paragragh_count}</td></tr>"
    content += "<tr><td>Sentences/Paragragh avg.</td>"
    content += "<td>#{sentence_count / paragragh_count}</td></tr>"
    content += "<tr><td>Words per Sentence Avg.</td><td>#{word_count / sentence_count}</td></tr>"
    content += "<tr><td>Non-fluff</td><td>#{good_percentage}%</td></tr></table>"
    content += "<h3>ABSTRACT</h3>"
    content += "<table><tr><td>#{ideal_sen_out.join(". ")}"
    content += "</td></tr></table>"
    content += "<h3>THE TEN MOST COMMON WORDS</h3>"
    content += "<table><tr><td>#{top_10.reverse[0,10]}</td></tr></table><hr>"
  end

# Exceptions will be caught here
rescue Exception => e
  content += "<pre>Stack Trace:"
  content += e.backtrace.join("<br />\n")
  content += "</pre>"
end

# Fill templates with string
html = head_html % [:title => 'Lab3.cgi Text Analyzer',:banner => header_html,:content => content]

# Print footer
print html + foot_html

# EOF
