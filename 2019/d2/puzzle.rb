require 'byebug'

def str_to_arr(str)
  arr = str.split(",")
  arr.map(&:to_i)
end

def comp(arr)
  op_idx = 0
  op = arr[op_idx]
  until op == 99
    in_idx1 = arr[op_idx + 1]
    in_idx2 = arr[op_idx + 2]
    in1 = arr[in_idx1]
    in2 = arr[in_idx2]
    out_idx = arr[op_idx + 3]
    if op == 1
      # debugger
      arr[out_idx] = in1 + in2
    elsif op == 2
      # debugger
      arr[out_idx] = in1 * in2
    end 
    # debugger
    op_idx += 4
    op = arr[op_idx]
  end 
  arr
end 

# str = IO.read('input.txt')
# arr = str_to_arr(str)
# print comp(arr)



a = 0 
b = 0
result = 0

while a < 100
  b = 0
  while b < 100
    str = IO.read('input.txt')
    arr = str_to_arr(str)
    arr[1] = a
    arr[2] = b
    result = comp(arr)[0]
    if result == 19690720
      puts a
      puts b 
    end 
    b += 1
  end 
  a += 1
end 