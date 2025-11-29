def heapify(arr,i,n):
     largest = i
     l = 2* i + 1
     r = 2* i + 2

     if l < n and arr[l] > arr[largest]:
        largest = l

     if r < n and arr[r] > arr[largest]:
       largest = r
    
     if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr,largest,n)

def main():
     arr = [10,5,15,2,20,30]
     print("Original array:", end ="")
     for i in range(len(arr)):
         print(arr[i], end="")

     for i in range(len(arr)//2 -1 ,-1,-1):
         heapify(arr,i,len(arr))