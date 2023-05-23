global Jobs
global NumberOfJobs

Jobs = [[0 for i in range(2)] for j in range(100)]  # global integer, 100 by 2 elements
NumberOfJobs = 0  # global integer


def Initialise():
    global Jobs
    global NumberOfJobs
    for i in range(100):
        for j in range(2):
            Jobs[i][j] = -1
    NumberOfJobs = 0


def AddJob(NewJobNumber, NewJobPriority):
    global Jobs
    global NumberOfJobs
    if NumberOfJobs >= 100:
        print("Not added")
    else:
        Jobs[NumberOfJobs][0] = NewJobNumber
        Jobs[NumberOfJobs][1] = NewJobPriority
        NumberOfJobs = NumberOfJobs + 1
        print("Added")


def InsertionSort():
    global Jobs
    global NumberOfJobs
    for i in range(1, NumberOfJobs):
        CurrentJob = Jobs[i][0]
        CurrentJobProirity = Jobs[i][1]

        NewIndex = i
        while (NewIndex > 0) and (CurrentJobProirity < Jobs[NewIndex - 1][1]):
            Jobs[NewIndex][0] = Jobs[NewIndex - 1][0]
            Jobs[NewIndex][1] = Jobs[NewIndex - 1][1]
            NewIndex = NewIndex - 1

        Jobs[NewIndex][0] = CurrentJob
        Jobs[NewIndex][1] = CurrentJobProirity


def PrintArray():
    global NumberOfJobs 
    global Jobs
    for i in range (NumberOfJobs):
        print (Jobs[i][0], " priority ", Jobs[i][1])

Initialise()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)

InsertionSort()
PrintArray()