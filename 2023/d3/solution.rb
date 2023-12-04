# PLAN:
# Iterate, once you hit a digit, keep going until you have full number
#
# On first iteration, store every number as: 
#   [number, [x,y], length] 
# (where x,y refers to index of first digit)
#
# Then iterate THAT list and for each number (using it's pos and len)
# determine if it has an adjacent symbol

INPUT = File.new('input.txt').readlines.map(&:chomp).map {|l| l.split("")}
X_LEN = INPUT.length
Y_LEN = INPUT.first.length

DIGITS = (0..9).map(&:to_s)


def get_nums
  found_nums = []
  INPUT.each_with_index do |line, x|
    in_num = false
    current_num = nil
    line.each_with_index do |char, y|
      if DIGITS.include?(char)
        if in_num
          current_num[0] += char
          current_num[2] += 1
        else
          in_num = true
          current_num = [char, [x,y], 1]
        end
      elsif current_num
        current_num[0] = current_num[0].to_i
        found_nums << current_num
        in_num = false
        current_num = nil
      end
    end

    if current_num
      current_num[0] = current_num[0].to_i
      found_nums << current_num
      in_num = false
      current_num = nil
    end
  end

  found_nums
end

def add_idxs_around(num_arr)
  x, y = num_arr[1]
  len = num_arr[2]
  res = []
  (x-1..x+1).each do |xx|
    (y-1..y+len).each do |yy|
      if xx >= 0 && xx < X_LEN && yy >= 0 && yy < Y_LEN
        res << [xx,yy]
      end
    end
  end

  num_arr << res
end

def valid?(num_arr)
  num_arr[3].each do |(x,y)|
    c = INPUT[x][y] 
    if !DIGITS.include?(c) && c != '.'
      return true
    end
  end

  false
end

def solve_p1
  nums = get_nums
  nums.each {|n| add_idxs_around(n)}
  nums.inject(0) {|acc, el| valid?(el) ? acc + el[0] : acc }
end

# PART 2

def find_gears(nums)
  gears = Hash.new {|h,k| h[k] = []}
  nums.each_with_index do |num, i|
    num[3].each do |(x,y)|
      c = INPUT[x][y] 
      if c == '*'
        gears[[x,y]] << nums[i][0]
      end
    end
  end
  gears
end

def solve_pt2
  nums = get_nums
  nums.each {|n| add_idxs_around(n)}
  gears = find_gears(nums)

  total = 0
  gears.each do |(_, nums)|
    next if nums.length < 2
    total += nums.inject(:*)
  end

  total
end

puts solve_pt2
