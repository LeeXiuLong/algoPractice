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


def productSum(array, multiplier = 1):
    currentSum = 0
    for item in array:
        if isinstance(item, list):
            currentSum += productSum(item, multiplier+1)
        else:
            currentSum += item
    return currentSum * multiplier

 def binarySearch(array, target):
     midIndex = int(len(array)/2)
     if len(array) == 0:
         return -1
     if array[midIndex] == target:
         return midIndex
     elif array[midIndex] > target:
         return binarySearch(array[:midIndex], target)
     else:
         upperBinary = binarySearch(array[midIndex+1:], target)
         return -1 if upperBinary == -1 else midIndex + 1 + upperBinary
     

def findThreeLargestNumbers(array):
    largest = float("-inf")
    middle = float("-inf")
    smallest = float("-inf")
    
    for number in array:
        if number >= largest:
            smallest = middle
            middle = largest
            largest = number
        elif number >= middle:
            smallest = middle
            middle = number
        elif number >= smaller:
            smallest = number
    
    return [smallest, middle, largest]

def bubbleSort(array):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                sorted = False
    return array

def insertionSort(array):
    for i in range(1, len(array)):
        sorted  = False
        current = i
        while not sorted and current > 0:
            if array[current] < array[current-1]:
                array[current], array[current-1] = array[current-1], array[current]
                current -= 1
            else:
                sorted = True
	return array
    
    
         

        
    