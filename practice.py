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

def selectionSort(array):
    for i in range(len(array)):
        lowest = i
        for j in range(i+1,len(array)):
            if array[lowest] > array[j]:
                lowest = j
        array[lowest], array[i] = array[i], array[lowest]
    return array

def isPalindrome(string):
    last = len(array)-1
    first = 0
    while first < last:
        if string[first] != string[last]:
            return False
        else:
            last -= 1
            first += 1
    return True

def caesarCipherEncryptor(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_string = ""
    for letter in string:
        letter_index = alphabet.index(letter)
        new_string += alphabet[(letter_index+key)%26]
    return new_string

def branchSums(root):
    if root == None:
        return []
    if self.left or self.right:
        new_list = branchSums(self.left) + branchSums(self.right)
        return_list = []
        for item in new_list:
            return_list.append(item + root.value)
        return return_list
    else:
        return [root.value]

[13458]
[24569]

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    red_shirt_greater = redShirtHeights[0] > blueShirtHeights[0]
    for i in range(len(redShirtHeights)):
        if redShirtHeights[i] > blueShirtHeights[i] != red_shirt_greater:
            return False
    return True 

def minimumWaitingTime(queries):
    queries.sort()
	total_sum = 0
	current_sum = 0
	for i in range(len(queries)-1):
		current_sum += queries[i]
		total_sum += current_sum
	return total_sum

def minimumWaitingOptimal(queries):
    queries.sort()
    total_sum = 0
    current_length = len(queries)-1
    for i in range(len(queries)-1):
        total_sum += queries[i] * current_length
        current_length -= 1
    return total_sum

def nodeDepths(root, depth = 0):
    if root == None: 
        return 0
    if root.right or root.left:
        return depth + nodeDepths(root.right, depth+1) + nodeDepths(root.left, depth+1)
    else:
        return depth

    
    This is a demo task.

#Write a function:

#def solution(A)that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

#Given A = [1, 2, 3], the function should return 4.

#Given A = [−1, −3], the function should return 1.

#Write an efficient algorithm for the following assumptions:

#N is an integer within the range [1..100,000]; each element of array A is an integer within the range [−1,000,000..1,000,000].
            
    
    
         

        
    