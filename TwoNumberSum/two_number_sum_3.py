def twoNumberSum(array, targetSum):
   array.sort()
   left = 0
   right = len(array) - 1
	
   while left < right:
      potentialMatch = array[left] + array[right]
      if potentialMatch == targetSum:
         return [array[left], array[right]]
      elif potentialMatch > targetSum:
         right -= 1
      else:
         left += 1

   return []