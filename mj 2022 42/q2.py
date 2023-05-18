import random

# IntegerArr [10][10]
ArrayData = [[0 for i in range(10)] for j in range(10)]

for i in range(10):
    for j in range(10):
        ArrayData[i][j] = random.randint(1, 100)


def PrintArray(ArrayData):
    for i in range(10):
        for j in range(10):
            print(ArrayData[i][j], end=" ")
        print("")


print("before sorting:")
PrintArray(ArrayData)

ArrayLength = 10
for x in range(0, ArrayLength):
    for y in range(0, ArrayLength - 1):
        for z in range(0, ArrayLength - y - 1):
            if ArrayData[x][z] > ArrayData[x][z + 1]:
                TempValue = ArrayData[x][z]
                ArrayData[x][z] = ArrayData[x][z + 1]
                ArrayData[x][z + 1] = TempValue

print("after sorting:")
PrintArray(ArrayData)



def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if (Upper >= Lower):
        Mid = int((Lower + (Upper)) // 2)
        if (SearchArray[0][Mid] == SearchValue):
            return Mid
        else:
            if (SearchArray[0][Mid] > SearchValue):
                return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
            else:
                return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)
    return -1


print(BinarySearch(ArrayData, 0, 9, 1))
# print ("-1")
print(BinarySearch(ArrayData, 0, 9, 18))
        