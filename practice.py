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

# this is a comment
