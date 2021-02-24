def twoNumberSum(array, targetSum):
    hashMap = {}
    for number in array:
        if number in hashMap:
            return [hashMap[number], number]
        else:
            hashMap[targetSum-number] = number
    
    return []

def twoNumberSum(array,targetSum):
    array.sort()
    leftPointer = 0
    rightPointer = array.length - 1
    while leftPointer < rightPointer:
        currentSum = array[leftPointer] + array[rightPointer]
        if currentSum == targetSum:
            return [array[leftPointer], array[rightPointer]]
        elif currentSum > targetSum:
            rightPointer -= 1
        else:
            leftPointer += 1
    return []


def findClosestValueInBst(tree,target):
    closest = tree.value
    currentBranch = tree
    
    while currentBranch != None:
        currentClosestDiff = abs(target-closest)
        currentDiff = abs(currentBranch.value - target)
        
        if currentClosestDiff > currentDiff:
            closest = currentBranch.value
            
        if currentBranch.value == target:
            return target
        elif currentBranch.value > target:
            currentBranch = currentBranch.left
        else:
            currentBranch = currentBranch.right
    
    return closest

def depthFirstSearch(self, array):
    array.append(self.name)
	if len(self.children) != 0:
		for child in self.children:
			child.depthFirstSearch(array)
	return array

def getNthFib(n):
    if n == 1:
        return 0
    if n == 2: 
        return 1
    else:
        return getNthFib(n-1) + getNthFib(n-2)



        
    