def twoNumberSum(array, targetSum):
	nums = {}
	
	for i in array:
		potentialMatch = targetSum - i
		
		if potentialMatch in nums:
			return [potentialMatch, i]
		else:
			nums[i] = True
		
	return []