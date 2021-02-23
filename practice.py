def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    pointer1 = 0
    pointer2 = 0
    smallest = float("inf")
    current = 0
    returnArr = []

    while pointer1 < len(arrayOne) and pointer2 < len(arrayTwo):
        current1 = arrayOne[pointer1]
        current2 = arrayTwo[pointer2]
        current = abs(current1 - current2)
        if current1 == current2:
            return [current1, current2]
        if current < smallest:
            smallest = current
            returnArr = [current1, current2]
        if current1 < current2:
            pointer1 += 1
        elif current2 < current1:
            pointer2 += 1
    return returnArr


def moveElementToEnd(array, toMove):
    currentPlace = 0
    for i in range(len(array)):
        if array[i] != toMove:
            array[i], array[currentPlace] = array[currentPlace], array[i]
            currentPlace += 1
    return array

def exampleFunction(argument):
    return argument + 2

def reviewForSyntax(argument):
    return argument

# this is a comment
#this is more stuff that i added

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
        
    