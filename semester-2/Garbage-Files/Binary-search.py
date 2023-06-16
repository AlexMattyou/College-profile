# same old

def search(array, target, start = 0, end = 0):
    if end == 0:
        end = len(array)
    mid = (start+end)//2
    if start == end:
        return -1
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return search(array,target,start,mid)
    elif array[mid] < target:
        return search(array,target,mid+1,end)

array = list(map(int,input('enter the sorted array: ').split()))
target = int(input('Target: '))
print(search(array, target))
