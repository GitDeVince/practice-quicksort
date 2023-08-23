
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array [0]
        less = [i for i in array [1:] if i <= pivot]
        greater = [i for i in array [1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

def getarray():
    number = int(input())
    
    if number == 0:
        return getarray
    else:
        for i in range(0, number):
           ele = int(input())
           sorting.append(ele)
       


sorting = []


print("Enter number of elements: ")
getarray()

print ("Your new sorted list: ")
print(quicksort(sorting))