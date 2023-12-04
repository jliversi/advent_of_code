INPUT = File.new("input.txt").readlines.map(&:chomp)

# Part 1
# def calc_line(line) 
#
#   _, nums = line.split(":")
#   winning, nums = nums.split("|")
#   winning = winning.split(" ").map(&:to_i)
#   nums = nums.split(" ").map(&:to_i)
#
#   total = 0
#   nums.each do |num|
#     if winning.include?(num)
#       if total < 1
#         total = 1
#       else
#         total *= 2
#       end
#     end
#   end
#   total
# end
#
# res = INPUT.map {|l| calc_line(l)}.sum
# puts res

# PART 2
def get_nums(line)
  _, nums = line.split(":")
  winning, nums = nums.split("|")
  winning = winning.split(" ").map(&:to_i)
  nums = nums.split(" ").map(&:to_i)

  [winning, nums]
end

COUNTS = [1] * INPUT.length
INPUT.each_with_index do |l, i|
  winning, nums = get_nums(l)
  wins = nums.count {|n| winning.include?(n) }
  wins.times do |j|
    idx = i + j + 1
    COUNTS[idx] += COUNTS[i] if idx < INPUT.length
  end
end

puts COUNTS.sum
