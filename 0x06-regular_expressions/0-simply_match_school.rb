#!/usr/bin/env ruby
def school(input)
  regex = /School/
  m = input.scan(regex).join
  puts m
end

if ARGV.empty?
  puts "Please provide an argument."
else
  i = ARGV[0]
  school(i)
end
