io.input("input.txt")

local mem = io.read("*a")

local op_pattern = "mul%(%d?%d?%d,%d?%d?%d%)"

local ops = string.gmatch(mem, op_pattern)

local function multiply(op_string)
  local res = 1
  for num in string.gmatch(op_string,"%d+") do
    res = res * tonumber(num)
  end
  return res
end

local ans1 = 0

for op in ops do
  ans1 = ans1 + multiply(op)
end

print("Part 1:", ans1)

local do_pattern = "do()"
local dont_pattern = "don't()"

local i = 1
local ops_on = true
local ans2 = 0

while i < string.len(mem) do
  local trigger_pattern = ops_on and dont_pattern or do_pattern
  local next_trigger_idx, end_trigger_idx = string.find(mem, trigger_pattern, i, true)
  local next_mul_idx, end_mul_idx = string.find(mem, op_pattern, i)

  if next_trigger_idx and next_trigger_idx < next_mul_idx then
    if not end_trigger_idx then break end
    ops_on = not ops_on
    i = end_trigger_idx
  else
    if ops_on and next_mul_idx then
      local op = string.sub(mem, next_mul_idx, end_mul_idx)
      ans2 = ans2 + multiply(op)
    end
    if not end_mul_idx then break end
    i = end_mul_idx
  end
end

print("Part 2:", ans2)
