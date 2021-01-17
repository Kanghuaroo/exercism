local Hamming = {}

function Hamming.compute(a,b)
	if a:len() ~= b:len() then
		return -1
	end

	local count = 0
	for i = 0, a:len() do
		if a:sub(i,i) ~= b:sub(i,i) then
			count = count + 1
		end
	end
	return count
end

return Hamming
