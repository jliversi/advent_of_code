local list1 = {}
local list2 = {}
for line in io.lines("input.txt") do
  local i = 0
  for digit in string.gmatch(line, "%d+") do
    local num = tonumber(digit)
    if i == 0 then
      table.insert(list1, num)
    else
      table.insert(list2, num)
    end
    i = 1
  end
end

table.sort(list1)
table.sort(list2)

local diffs = {}

for i, v in ipairs(list1) do
  local v1 = v
  local v2 = list2[i]
  local diff = math.abs(v2 - v1)
  table.insert(diffs, diff)
end

local sum = 0
for _, v in ipairs(diffs) do
  sum = sum + v
end

-- PART 2 --

local counts = {}
for _, v in ipairs(list2) do
  if counts[v] then
    counts[v] = counts[v] + 1
  else
    counts[v] = 1
  end
end

local result = 0
for _, v in ipairs(list1) do
  local count = counts[v] or 0
  local score = count * v
  result = result + score
end

print(result)
