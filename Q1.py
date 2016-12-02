import random

List123 = [7,5,1,3,9,6,2,4] 
shuffledList = []

while(List123!=[]):
    n = random.randint(0, len(List123)-1)
    shuffledList.append(List123[n]) 
    del List123[n]

print(shuffledList)
