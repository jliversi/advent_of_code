input = File.new('input.txt').readlines.map(&:chomp)

# PART 1

COLORS = %w[red green blue]
COLOR_COUNTS = [12, 13, 14]

def convert_line(line)
  id, rest = line.split(":")
  id = id.sub("Game ", "").to_i

  samples = rest.split(";")
  results = []
  samples.each do |s|
    x = [0,0,0]
    s.split(",").each do |c|
      num, color = c.split(" ")
      x[COLORS.index(color)] = num.to_i
    end

    results << x
  end

  [id, results]
end

input.map! {|l| convert_line(l) }

def valid?(all_counts)
  all_counts.each do |counts|
    counts.each_with_index do |c, i|
      return false if c > COLOR_COUNTS[i]
    end
  end

  true
end

puts input.inject(0) { |acc, el| valid?(el[1]) ? acc + el[0] : acc }

# PART 2
def power(counts)
  counts.transpose.map(&:max).inject(&:*)
end

puts input.inject(0) { |acc, el| acc + power(el[1]) }
