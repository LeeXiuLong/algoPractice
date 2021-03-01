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


#second attempt
def insertionSort(array):
    for i in range(1, len(array)):
        current = i
        while array[current] < array[current-1] and current > 0:
            array[current], array[current-1] = array[current-1], array[current]
            current -= 1
    return array

#2nd attempt
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    difference = redShirtHeights[0] > blueShirtHeights[0]
    for i in range(len(redShirtHeights)):
        currentRed = redShirtHeights[i]
        currentBlue = blueShirtHeights[i]
        if (currentRed > currentBlue) != difference or currentRed == currentBlue:
            return False
    return True

#In the beginning the current Change that you're keeping track of should be zero
#after sorting the array if the current element of the array is greater than the current Change+1
# you cannot make currentChange + 1
# this makes sense as in order to make the currentChange + 1 you would need sometihng equal to that amount or less
#in order to make all the values in between. 
def nonConstructibleChange(coins):
    coins.sort()
    currentChange = 0
    for item in coins:
        if item > currentChange + 1:
            return currentChange + 1
        else:
            currentChange += item
    return currentChange + 1


    
    
            
    
    
         

        
    