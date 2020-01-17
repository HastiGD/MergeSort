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
        middleIndex = (listLength//2)

        # divide list into left and right
        left = List[:middleIndex]
        right = List[middleIndex:]
        print(left, right)

        # call MergeSort on each half
        MergeSort(left)
        MergeSort(right)

        # merge the left and right sorted lists
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                List[k] = left[i]
                i = i + 1
            else:
                List[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            List[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            List[k] = right[j]
            j = j + 1
            k = k + 1

        print(List)

def main():

    List = createList(10)
    print(List)
    MergeSort(List)
    print(List)

main()