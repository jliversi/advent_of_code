require 'byebug'
require 'set'

# puts in1
# puts in2

def build_nodes_one(in_str)
    set = Set.new
    x,y = [0,0]
    in_str.each do |str|
        dir = str[0]
        num = str[1..-1].to_i
        case dir 
        when "R"
            r = (x..(x + num))
            r.each do |i|
                set.add([i, y])
                x = i
            end 
        when "L"
            r = ((x - num)...x)
            r.to_a.reverse.each do |i|
                set.add([i, y])
                x = i
            end 
        when "U"
            r = (y..y + num)
            r.each do |i|
                set.add([x, i])
                y = i
            end 
        when "D"
            r = ((y - num)...y)
            r.to_a.reverse.each do |i|
                set.add([x, i])
                y = i
            end 
        end 
    end 
    set
end 

def build_nodes_if_in_one(in_str, in_set)
    set = []
    x,y = [0,0]
    in_str.each do |str|
        dir = str[0]
        num = str[1..-1].to_i
        case dir 
        when "R"
            r = (x..(x + num))
            r.each do |i|
                set.push([i, y]) if in_set.include?([i, y])
                x = i
            end 
        when "L"
            r = ((x - num)...x)
            r.to_a.reverse.each do |i|
                set.push([i, y]) if in_set.include?([i, y])
                x = i
            end 
        when "U"
            r = (y..y + num)
            r.each do |i|
                set.push([x, i]) if in_set.include?([x, i])
                y = i
            end 
        when "D"
            r = ((y - num)...y)
            r.to_a.reverse.each do |i|
                set.push([x, i]) if in_set.include?([x, i])
                y = i
            end 
        end 
    end 
    set
end 

def calc_dist_one(x, y)
    x.abs + y.abs
end 

def complete_one(in1, in2)
    arr1 = build_nodes_one(in1)
    arr2 = build_nodes_if_in_one(in2, arr1)
    arr2.map! {|el| calc_dist_one(el[0], el[1])}
    arr2.reject! {|el| el == 0}
    arr2.min
end 

# str1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",")
# str2 = "U62,R66,U55,R34,D71,R55,D58,R83".split(",")

# str1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(",")
# str2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(",")

# puts complete(str1, str2)

# test = "R8,U5,L5,D3".split(",")
# a = build_nodes(test)
# a.each do |el|
#     print el
#     puts
# end 


def build_nodes_two(in_str)
    hash = Hash.new
    x,y = [0,0]
    dx, dy = [0,0]
    in_str.each do |str|
        dir = str[0]
        num = str[1..-1].to_i
        case dir 
        when "R"
            r = (x + 1..(x + num))
            r.each do |i|
                dx += 1
                hash[[i,y]] = (dx + dy)
                x = i
            end 
        when "L"
            r = ((x - num)...x)
            r.to_a.reverse.each do |i|
                dx += 1
                hash[[i,y]] = (dx + dy)
                x = i
            end 
        when "U"
            r = (y + 1..y + num)
            r.each do |i|
                dy += 1
                hash[[x,i]] = (dx + dy)
                y = i
            end 
        when "D"
            r = ((y - num)...y)
            r.to_a.reverse.each do |i|
                dy += 1
                hash[[x,i]] = (dx + dy)
                y = i
            end 
        end 
    end 
    hash
end 

def build_nodes_if_in_two(in_str, in_hash)
    hash = Hash.new
    x,y = [0,0]
    dx, dy = [0,0]
    in_str.each do |str|
        dir = str[0]
        num = str[1..-1].to_i
        case dir 
        when "R"
            r = (x + 1..(x + num))
            r.each do |i, idx|
                dx += 1
                if in_hash.has_key?([i, y])
                    hash[[i,y]] = (dx + dy)
                end 
                x = i
            end 
        when "L"
            r = ((x - num)...x)
            r.to_a.reverse.each do |i, idx|
                dx += 1
                if in_hash.has_key?([i, y])
                    hash[[i,y]] = (dx + dy)
                end 
                x = i
            end 
        when "U"
            r = (y + 1..y + num)
            r.each do |i, idx|
                dy += 1
                if in_hash.has_key?([x,i])
                    hash[[x,i]] = (dx + dy)
                end 
                y = i
            end 
        when "D"
            r = ((y - num)...y)
            r.to_a.reverse.each do |i, idx|
                dy += 1
                if in_hash.has_key?([x,i])
                    hash[[x,i]] = (dx + dy)
                end 
                y = i
            end 
        end 
    end 
    hash
end 

def calc_dist_two(x, y)
    x + y
end 

def complete_two(in1, in2)
    hash1 = build_nodes_two(in1)
    puts hash1
    hash2 = build_nodes_if_in_two(in2, hash1)
    puts hash2
    arr = []
    hash1.each do |k,v|
        # debugger
        if hash2.has_key?(k)
            arr.push(v + hash2[k])
        end 
    end 
    arr.reject! {|el| el == 0}
    arr.min
end 

# one = "R8,U5,L5,D3".split(",")
# two = "U7,R6,D4,L4".split(",")

# one = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",")
# two = "U62,R66,U55,R34,D71,R55,D58,R83".split(",")

# one = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(",")
# two = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(",")

# puts complete_two(one, two)



inputs = File.new('input.txt').readlines.map(&:chomp).map { |str| str.split(",") }
in1 = inputs[0]
in2 = inputs[1]

puts complete_two(in1, in2)