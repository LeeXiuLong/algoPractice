def twoNumberSum(array, targetSum):
    hashMap = {}
    for number in array:
        if number in hashMap:
            return [hashMap[number], number]
        else:
            hashMap[targetSum-number] = number

    return []


def twoNumberSum(array, targetSum):
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


def findClosestValueInBst(tree, target):
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


def productSum(array, multiplier=1):
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


# second attempt
def insertionSort(array):
    for i in range(1, len(array)):
        current = i
        while array[current] < array[current-1] and current > 0:
            array[current], array[current-1] = array[current-1], array[current]
            current -= 1
    return array

# 2nd attempt
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

# In the beginning the current Change that you're keeping track of should be zero
# after sorting the array if the current element of the array is greater than the current Change+1
# you cannot make currentChange + 1
# this makes sense as in order to make the currentChange + 1 you would need sometihng equal to that amount or less
# in order to make all the values in between. 
def nonConstructibleChange(coins):
    coins.sort()
    currentChange = 0
    for item in coins:
        if item > currentChange + 1:
            return currentChange + 1
        else:
            currentChange += item
    return currentChange + 1

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    prevNode = None
    while currentNode != None:
        if prevNode:
            if currentNode.value == prevNode.value:
                prevNode.next = currentNode.next
            else:
                prevNode = currentNode
        else:
            prevNode = currentNode
        currentNode = currentNode.next
    return linkedList


def runLengthEncoding(string):
    currentLetter = string[0]
    currentCount = 0
    newString = ""
    for i in range(len(string)):
        if string[i] == currentLetter and currentCount < 9:
            currentCount += 1
        else:
            newString += str(currentCount) + currentLetter
            currentLetter = string[i]
            currentCount = 1
        if i == len(string)-1:
            newString += str(currentCount) + currentLetter
    return newString



    
    This is a demo task.

# Write a function:

# def solution(A)that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000]; each element of array A is an integer within the range [−1,000,000..1,000,000].
            
    

def generateDocument(characters, document):
    newHash = {}
    for item in characters:
        if item in newHash:
            newHash[item] += 1
        else:
            newHash[item] = 1
    for item in document:
        if item in newHash:
            if newHash[item] > 0:
                newHash[item] -= 1
            else:
                return False
        else:
            return False
	return True


def sortedSquaredArray(array):
    returnArray = []
    first = 0
    last = len(array)-1
    
    while first < last:
        firstNumber = array[first] * array[first]
        lastNumber = array[last] * array[last]
        
        if firstNumber < lastNumber:
            returnArray.push(lastNumber)
            last -= 1
        else:
            returnArray.push(firstNumber)
            first += 1
    return returnArray

def tournamentWinner(competitions, results):
    	currentBest = ""
	teamScores = {"": 0}

	for i in range(len(competitions)):
		home = competitions[i][0]
		away = competitions[i][1]
		winner = home if results[i] == 1 else away
		if winner not in teamScores:
			teamScores[winner] = 0
		teamScores[winner] += 3
		if teamScores[winner] > teamScores[currentBest]:
			currentBest = winner
	return currentBest
        
def isValidSubsequence(array, sequence):
	if len(sequence) == 0:
    		return True
	else:
		for i in range(len(array)):
			if array[i] == sequence[0]:
				return isValidSubsequence(array[i+1:], sequence[1:])
	return False

# practiced ruby models and migrations
# practicing this solution again
def minimumWaitingTime2(array):
    array.sort()
    total = 0
    currentSum = 0
    for i in range(len(array)-1):
        currentSum += array[i]
        total += currentSum
    return total

def nonConstructibleChange(coins):
    currentSum = 0
    coins.sort()
    for coin in coins:
        if coin > currentSum + 1:
            return currentSum + 1
        else:
            currentSum += coin
    return currentSum + 1
        

        
    def twoNumberSum(array, targetSum):
        dictionary = {}
        
        for item in array:
            if item in dictionary:
                return [item, dictionary[item]]
            else:
                dictionary[targetSum - item] = item
                
        return []


# define our closest variable
# make a recursive function with our closest as a param
# check if our current head is equal to target
# return head if equal to target
# check if our current head is closer to target than current closest
# update closest
# check if our current head is greater or lesser than our target
# move our tree to the node that corresponds to greater or lesser

def findClosestValueInBst(tree, target, closest=float("inf")):
    
    # making our variables
    currentClosestDistance = abs(closest-target)
    newClosest = closest
    
    # check to see if current value equals target
    if tree.value == target:
        return tree.value 

    # check to see if we need to update our closest
    if abs(target - tree.value) < currentClosestDistance:
        newClosest = tree.value
    
    # determine which tree to navigate to
    if tree.value > target:
        nextTree = tree.left
    else:
        nextTree = tree.right
        
    # if our tree is done then return our closest
    return newClosest if nextTree == None else findClosestValueInBst(nextTree, target, newClosest)


def depthFirstSearch(self, array):
    array.append(self.name)
    for child in self.children:
        child.depthFirstSearch(array)
    return array
    
