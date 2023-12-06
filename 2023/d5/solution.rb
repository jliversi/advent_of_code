INPUT = File.new("input.txt").read.split("\n\n")

SEEDS_1 = INPUT[0].split(" ")[1..].map(&:to_i)
SEEDS = SEEDS_1.each_slice(2).map {|pair| (pair[0]...(pair[0] + pair[1]))}

MAPS = INPUT[1..].map do |l|
  l = l.split("\n")
  res = {}

  res[:source], res[:dest] = l[0].split(" ")[0].split("-to-")

  l[1..].each do |nums|
    d, s, r = nums.split(" ").map(&:to_i)
    # res[(d...(d + r))] = (s...(s + r))
    res[(s...(s + r))] = [d,r]
  end

  res
end

def next_num(source_num, map)
  map.keys.each do |k|
    next if k == :source || k === :dest
    if k.include?(source_num) # k = (50...98), v = [52, 48], source_num = 79
      dest = (map[k][0] - k.first) + source_num 
      return dest
    end
  end

  source_num
end

def solve_pt1
  SEEDS.map do |seed|
    cur_num = seed
    MAPS.each do |map|
      # puts cur_num, map[:source], map[:dest]
      cur_num = next_num(cur_num, map)
    end

    cur_num
  end.min
end

print SEEDS.inject(0) {|acc, el| acc + el.size}
