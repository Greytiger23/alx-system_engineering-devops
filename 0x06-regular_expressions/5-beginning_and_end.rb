#!/usr/bin/env ruby
def pattern(input)
  regex = /^h.n$/
  m = input.scan(regex).join
  puts m
end

if ARGV.empty?
  puts "Please provide an argument."
else
  i = ARGV[0]
  pattern(i)
end
