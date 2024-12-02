local reports = {}

for line in io.lines("input.txt") do
	local report = {}
	for digit in string.gmatch(line, "%d+") do
		local num = tonumber(digit)
		table.insert(report, num)
	end
	table.insert(reports, report)
end

local function safeReport(report)
	local dir = report[1] < report[2] and 1 or -1

	for i, v in ipairs(report) do
		if i > 1 then
			local diff = v - report[i - 1]
			local abs_diff = math.abs(diff)
			if abs_diff < 1 or abs_diff > 3 then
				return false
			end

			if diff * dir < 0 then
				return false
			end
		end
	end

	return true
end

local total_safe = 0
for _, report in ipairs(reports) do
	if safeReport(report) then
		total_safe = total_safe + 1
	end
end

print("Part 1:", total_safe)

-- PART 2

local function safeReportWithRemoval(report)
	if safeReport(report) then
		return true
	end

	for i, v in ipairs(report) do
		local reportWithoutV = {}
		for i2, v2 in ipairs(report) do
			if i2 ~= i then
				table.insert(reportWithoutV, v2)
			end
		end
		if safeReport(reportWithoutV) then
			return true
		end
	end
end

total_safe = 0
for _, report in ipairs(reports) do
	if safeReportWithRemoval(report) then
		total_safe = total_safe + 1
	end
end

print("Part 2:", total_safe)
