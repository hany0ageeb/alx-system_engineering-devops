#!/usr/bin/env ruby
if matches = /\[from:(?<sender>[A-Za-z0-9+\-:]*)\].*\[to:(?<receiver>[A-Za-z0-9+\-:]*)\].*\[flags:(?<flags>[0-9a-zA-Z\-+:]*)\]/.match(ARGV[0])
  puts "#{matches['sender']},#{matches['receiver']},#{matches['flags']}"
end
