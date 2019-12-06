require 'byebug'

def run_machine(str, start_input)
    ints = parse_input(str)
    input = start_input
    
    cur_op_idx = 0

    loop do
        op_code = ints[cur_op_idx].to_s.reverse
        cur_op = op_code[0..1].reverse.to_i

        mode1 = op_code[2] || 0
        mode2 = op_code[3] || 0

        mode1 = mode1.to_i
        mode2 = mode2.to_i

        mode1 = mode1 == 0
        mode2 = mode2 == 0

        case cur_op
        when 1
            in1_idx = ints[cur_op_idx + 1]
            in2_idx = ints[cur_op_idx + 2]
            in1 = mode1 ? ints[in1_idx] : in1_idx
            in2 = mode2 ? ints[in2_idx] : in2_idx
            out_idx = ints[cur_op_idx + 3]
            ints[out_idx] = in1 + in2
            cur_op_idx += 4
        when 2
            in1_idx = ints[cur_op_idx + 1]
            in2_idx = ints[cur_op_idx + 2]
            in1 = mode1 ? ints[in1_idx] : in1_idx
            in2 = mode2 ? ints[in2_idx] : in2_idx
            out_idx = ints[cur_op_idx + 3]
            ints[out_idx] = in1 * in2
            cur_op_idx += 4
        when 3
            in1_idx = ints[cur_op_idx + 1]
            ints[in1_idx] = input
            cur_op_idx += 2
        when 4
            in1_idx = ints[cur_op_idx + 1]
            in1 = mode1 ? ints[in1_idx] : in1_idx
            puts in1
            cur_op_idx += 2
        when 5
            in1_idx = ints[cur_op_idx + 1]
            in2_idx = ints[cur_op_idx + 2]
            in1 = mode1 ? ints[in1_idx] : in1_idx
            in2 = mode2 ? ints[in2_idx] : in2_idx
            if in1 != 0
                cur_op_idx = in2
            else 
                cur_op_idx += 3
            end 
        when 6
            in1_idx = ints[cur_op_idx + 1]
            in2_idx = ints[cur_op_idx + 2]
            in1 = mode1 ? ints[in1_idx] : in1_idx
            in2 = mode2 ? ints[in2_idx] : in2_idx
            if in1 == 0
                cur_op_idx = in2
            else 
                cur_op_idx += 3
            end 
        when 7
            in1_idx = ints[cur_op_idx + 1]
            in2_idx = ints[cur_op_idx + 2]
            out_idx = ints[cur_op_idx + 3]
            in1 = mode1 ? ints[in1_idx] : in1_idx
            in2 = mode2 ? ints[in2_idx] : in2_idx

            ints[out_idx] = in1 < in2 ? 1 : 0
            cur_op_idx += 4
        when 8
            in1_idx = ints[cur_op_idx + 1]
            in2_idx = ints[cur_op_idx + 2]
            out_idx = ints[cur_op_idx + 3]
            in1 = mode1 ? ints[in1_idx] : in1_idx
            in2 = mode2 ? ints[in2_idx] : in2_idx

            ints[out_idx] = in1 == in2 ? 1 : 0
            cur_op_idx += 4
        when 9
            break
        when 99
            break
        end 
    end
end 

def parse_input(str)
    str.split(",").map(&:to_i)
end 

input = File.new('input.txt').readlines[0]
# input = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"



run_machine(input, 5)