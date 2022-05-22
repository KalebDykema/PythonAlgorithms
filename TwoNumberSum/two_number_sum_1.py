def twoNumberSum(array, targetSum):
   for i in range(len(array)):
      first = array[i]
      for j in range(len(array)):
         second = array[j]
         potentialMatch = first + second
         if potentialMatch == targetSum and i != j:
            return [first, second]
			
   return []