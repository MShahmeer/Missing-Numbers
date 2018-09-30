import random
import time

numArray = []

arrayRange = 100000000
randomExclusion = random.randint(1, arrayRange)

print("Creating array...")
arrayStart = time.time()
for i in range(1, arrayRange):
    if i != randomExclusion:
        numArray.append(i)
        #print((i/arrayRange)*100)

print("Done making array of length " + str(len(numArray)) + " in " + str(time.time() - arrayStart) + " seconds")

print("Working through linear search:")
linearTimeStart = time.time()
for i in range(0, len(numArray)):
    if numArray[i] != (i + 1):
        print("The missing number is " + str(numArray[i] - 1))
        break
print("Found missing number with linear search  in " + str(time.time() - linearTimeStart) + " seconds")

print("Working through binary search:")
missingNumFound = False
binaryTimeStart = time.time()
while missingNumFound == False:
    middleIndex = int(len(numArray)/2)
    half = numArray[:middleIndex]
    if numArray[middleIndex] - numArray[middleIndex - 1] == 1:
        if len(half) - (half[len(half) - 1] - half[0]) == 1:
            numArray = numArray[middleIndex:]
        else:
            numArray = numArray[:middleIndex]
    else:
        print("The missing number is " + str(numArray[middleIndex] - 1))
        missingNumFound = True
print("Found missing number with binary search in " + str(time.time() - binaryTimeStart) + " seconds")