input = File.new('input.txt').readlines.map(&:chomp)

# PART 1
# total = 0
# input.each do |line|
#   line.gsub!(/[A-Za-z]/, "")
#   total += (line[0] + line[-1]).to_i
# end
#
# puts total


# PART 2
total = 0
num_strings = [
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine",
  "1",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "9"
]

first_num_regex = Regexp.new(num_strings.join("|"))
last_num_regex = Regexp.new(num_strings.map(&:reverse).join("|"))


total = 0
input.each do |line|
  first_num = line[first_num_regex]
  last_num = line.reverse[last_num_regex].reverse
  first_num = first_num.to_i > 0 ? first_num : num_strings[num_strings.index(first_num) + 9]
  last_num = last_num.to_i > 0 ? last_num : num_strings[num_strings.index(last_num) + 9]
  total += (first_num + last_num).to_i
end

puts total
