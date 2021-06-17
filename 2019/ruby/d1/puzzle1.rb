arr = File.new('input1.txt').readlines.map(&:chomp).map(&:to_i)

def calc_fuel(num)
  (num/3) - 2
end

def full_calc(num)
  sum = 0
  latest = calc_fuel(num)
  while latest > 0
    sum += latest
    latest = calc_fuel(latest)
  end
  sum
end


arr.map! do |num|
  full_calc(num)
end 

sum = arr.inject(&:+)
puts sum
# latest = sum
# while latest > 0
#   latest = calc_fuel(latest)

# end
