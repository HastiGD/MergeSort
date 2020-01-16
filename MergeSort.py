import random

# createList        creates an unsorted list of random integers
# input: n          integer specifying the length of the list
def createList(n):

    unsortedList = []

    for i in range(0, n):
        x = random.randint(-50, 50)
        unsortedList.append(x)

    return unsortedList

def MergeSort(List):

    listLength = len(List)

    if listLength > 1:
        # find index of middle
        middleIndex = (listLength//2)-1
        middleRight = middleIndex+1

        # divide list into left and right
        left = List[:middleRight]
        right = List[middleRight:]
        print(left, right)

        # call MergeSort on each half
        MergeSort(left)
        MergeSort(right)

        # merge lists


def main():

    List = createList(10)
    print(List)

    MergeSort(List)


main()