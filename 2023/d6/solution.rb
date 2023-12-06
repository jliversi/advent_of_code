TIMES, DISTANCES = File.new("input.txt").readlines.map(&:chomp).map {|el| el.split(" ")[1..].map(&:to_i) }

# pt 1
# total = 1
# TIMES.each_with_index do |t,i|
#   d = DISTANCES[i]
#
#   res = [
#     (((-t + Math.sqrt(t**2 - (4*d))).to_f / -2) + 0.000001).ceil,
#     (((-t - Math.sqrt(t**2 - (4*d))).to_f / -2) - 0.000001).floor,
#   ]
#
#   total *= res[1] - res[0] + 1
# end

t = TIMES.join("").to_i
d = DISTANCES.join("").to_i
total = 1
res = [
  (((-t + Math.sqrt(t**2 - (4*d))).to_f / -2) + 0.000001).ceil,
  (((-t - Math.sqrt(t**2 - (4*d))).to_f / -2) - 0.000001).floor,
]

total *= res[1] - res[0] + 1

puts total
