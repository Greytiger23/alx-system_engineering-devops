#!/usr/bin/env ruby
def school(input)
  regex = /School$/
  if input =~ regex
    puts "#{input}$"
  else
    puts "$"
  end
end

if ARGV.empty?
  puts "Please provide an argument."
else
  i = ARGV[0]
  school(i)
end
