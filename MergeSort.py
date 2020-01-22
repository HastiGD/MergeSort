import random

# createList        creates an unsorted list of random integers
# input: n          integer specifying the length of the list
def createList(n):

    unsortedList = []

    for i in range(0, n):
        x = random.randint(-50, 50)
        unsortedList.append(x)

    return unsortedList

# MergeSort         uses the divide and conquer technique to sort an unsorted list of random integers
# input: List       an unsorted list of random integers
def MergeSort(List):

    listLength = len(List)

    if listLength > 1:
        # find index of middle
        middleIndex = (listLength//2)

        # divide list into left and right
        left = List[:middleIndex]
        right = List[middleIndex:]

        # call MergeSort on each half
        MergeSort(left)
        MergeSort(right)

        # index for iterating through left and right halves
        i = j = 0

        # index for iterating through List
        k = 0

        # compare first element in the left list to the elements in the right list iteratively
        # put smaller of two elements in List
        # repeat until one of the lists is consumed
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                List[k] = left[i]
                i += 1
            else:
                List[k] = right[j]
                j += 1
            k += 1

        # add remaining elements from left list iteratively, if any exist
        while i < len(left):
            List[k] = left[i]
            i += 1
            k += 1

        # add remaining elements from right list iteratively, if any exist
        while j < len(right):
            List[k] = right[j]
            j += 1
            k += 1

# driver code for MergeSort
def main():

    numElements = 100
    str1 = "Unsorted list is : "
    str2 = "Sorted list is   : "

    List = createList(numElements)
    print(str1, List)
    MergeSort(List)
    print(str2, List)

main()