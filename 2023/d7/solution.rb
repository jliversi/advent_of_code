INPUT = IO.readlines("input.txt", chomp: true).map do |line|
  res = line.split(" ")
  res[1] = res[1].to_i
  res
end

# PART 1
# RANKS = "AKQJT98765432".split("")
#
# def hand_type(hand)
#   char_counts = Hash.new(0)
#   hand.each_char {|c| char_counts[c] += 1}
#   char_counts = char_counts.values.sort {|a,b| b <=> a}
#   f = char_counts[0]
#   # [5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1]
#   if f == 5
#     return 6
#   elsif f == 4
#     return 5
#   elsif f == 3 && char_counts.length == 2
#     return 4
#   elsif f == 3
#     return 3
#   elsif f == 2 && char_counts.length == 3
#     return 2
#   elsif f == 2
#     return 1
#   else
#     return 0
#   end
# end

# PART 2
RANKS = "AKQT98765432J".split("")

def hand_type(hand)
  char_counts = Hash.new(0)
  hand.each_char {|c| char_counts[c] += 1}
  j_count = char_counts.delete("J") || 0
  return 6 if j_count == 5
  char_counts = char_counts.values.sort {|a,b| b <=> a}
  char_counts[0] += j_count
  f = char_counts[0]
  # [5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1]
  if f == 5
    return 6
  elsif f == 4
    return 5
  elsif f == 3 && char_counts.length == 2
    return 4
  elsif f == 3
    return 3
  elsif f == 2 && char_counts.length == 3
    return 2
  elsif f == 2
    return 1
  else
    return 0
  end
end

def compare_hands(h1, h2)
  h1_type, h2_type = hand_type(h1), hand_type(h2)
  if h1_type == h2_type
    h1.length.times do |i|
      c1 = RANKS.index(h1[i])
      c2 = RANKS.index(h2[i])
      next if c1 == c2
      return c2 <=> c1
    end
  else
    return h1_type <=> h2_type
  end
  return 0
end

sorted_hands = INPUT.sort do |h1, h2|
  compare_hands(h1[0], h2[0])
end

total = 0
sorted_hands.each_with_index {|h,i| total += h[1] * (i + 1) }
puts total
