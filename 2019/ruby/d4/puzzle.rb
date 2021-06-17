require 'byebug'
def always_up(str)
    nums = str.split("")
    str.each_char.with_index do |c, i|
        if i != 0
            return false unless c.to_i >= str[i - 1].to_i
        end
    end 
    true
end 

def has_two_adj(str)
    nums = str.split("")
    str.each_char.with_index do |c, i|
        c = c.to_i
        if i != 0
            return true if c == str[i - 1].to_i
        end
    end 
    false
end

def has_only_two_adj(str)
    # nums = str.split("")
    # result = false
    # str.each_char.with_index do |c, i|
    #     c = c.to_i
    #     debugger
    #     if i > 0
    #         debugger
    #         if i > 1 && c != str[i - 1] && result == true
    #             debugger
    #             return true 
    #         end
    #         result = true if c == str[i - 1].to_i
    #         if i > 1
    #             debugger
    #             result = false if c == str[i - 2].to_i
    #         end
    #     end
    # end 
    # result

    nums = str.split("")
    arr = []
    cur = nums[0]
    count = 0
    nums.each_with_index do |num,i|
        if num != cur
            arr << count
            count = 1
            cur = num
        else 
            count += 1
        end 
    end 
    arr << count
    # print arr
    arr.include?(2)
end

num = 0
check = 278384
ending = 824795

while check <= ending 
    str = check.to_s
    if always_up(str) && has_only_two_adj(str)
        num += 1
    end
    # if always_up(str) && !has_only_two_adj(str)
    #     puts str
    # end 
    check += 1
end 

puts num