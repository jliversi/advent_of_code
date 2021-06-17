require 'byebug'

class OrbitNode
    attr_accessor :val, :parent, :children
    def initialize(val,parent = nil, children = [])
        @val = val
        @parent = parent
        @children = children
    end
    
    def inspect
        "#{parent} -> #{val}"
    end 
    def to_s
        val
    end 

    def add_child(child)
        child.parent = self
        children.push(child)
    end

    def add_parent(parent)
        parent.add_child(self)
    end

    def bf_traverse(&prc)
        queue = [self]
        until queue.empty? 
            current = queue.shift
            queue.concat(current.children)
            prc.call(current)
        end 
        nil
    end

    def num_orbits
        current = self 
        count = 0
        while current.parent
            count += 1
            current = current.parent
        end
        count
    end

    def count_all
        count = 0
        self.bf_traverse do |node|
            count += node.num_orbits
        end 
        count
    end 
end

def parse_line(str)
    str.split(")")
end 

def build_tree(inputs)
    hash = Hash.new
    inputs.map! {|el| parse_line(el) }
    inputs.each do |el|
        parent, child = el
        if hash[child]
            child = hash[child]
        else 
            child = OrbitNode.new(el[1])
            hash[el[1]] = child
        end 

        if hash[parent]
            parent = hash[parent]
            parent.add_child(child)
        else 
            parent = OrbitNode.new(parent)
            hash[el[0]] = parent
            parent.add_child(child)
        end
    end
    result = hash.values.select {|el| el.parent == nil }
    result[0]
end 

# test_input = File.new('test_input.txt').readlines.map(&:chomp)
# root = build_tree(test_input)
# puts root.count_all

input = File.new('input.txt').readlines.map(&:chomp)
root = build_tree(input)
# puts "answer 1"
# puts root.count_all


# puts "answer 2"
san_parents = []
you_parents = []
root.bf_traverse do |node|
    if node.val == "SAN" 
        node = node.parent
        while node.parent
            san_parents << node
            node = node.parent
        end
    elsif node.val == "YOU"
        node = node.parent
        while node.parent
            you_parents << node
            node = node.parent
        end
    end
end

sum1 = nil
sum2 = nil
san_parents.each_with_index do |el, i|
    j = you_parents.index(el)
    if j
        sum1 = j + i
        break
    end
end
you_parents.each_with_index do |el, i|
    j = san_parents.index(el)
    if j
        sum2 = j + i
        break
    end
end
puts sum1
puts sum2 