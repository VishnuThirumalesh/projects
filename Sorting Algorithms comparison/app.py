import time
import random 
import MergeSort
import HeapSort
import InsertionSort
import SelectionSort
import BubbleSort
import QuickSort
import QuickSortTM

Best = dict()
length = int(input("Size of array :"))
# Call for MergeSort
print("Merge Sort :")
arr = random.sample(range(1, length+1), length)
print("Length of array is " + str(len(arr)))
print("Actual Array :")
print(arr)
start = float(time.time())
print("Sorted Array :")
print(MergeSort.MergeSort(arr))           
end = float(time.time())
print("Execution time")
print(str(float(end - start)) + str("s"))
Best['MergeSort'] = str(float(end - start))

# # Call for HeapSort
print("Heap Sort :")
arr = random.sample(range(1, length+1), length)
print("Length of array is " + str(len(arr)))
print("Actual Array :")
print(arr)
start = float(time.time())
print("Sorted Array :")
print(HeapSort.HeapSort(arr))           
end = float(time.time())
print("Execution time")
print(str(float(end - start)) + str("s"))
Best['HeapSort'] = str(float(end - start))

# # Call for InsertionSort
print("Insertion Sort :")
arr = random.sample(range(1, length+1), length)
print("Length of array is " + str(len(arr)))
print("Actual Array :")
print(arr)
start = float(time.time())
print("Sorted Array :")
print(InsertionSort.InsertionSort(arr))           
end = float(time.time())
print("Execution time")
print(str(float(end - start)) + str("s"))
Best['InsertionSort'] = str(float(end - start))

# Call for SelectionSort
print("Selection Sort :")
arr = random.sample(range(1, length+1), length)
print("Length of array is " + str(len(arr)))
print("Actual Array :")
print(arr)
start = float(time.time())
print("Sorted Array :")
print(SelectionSort.SelectionSort(arr))           
end = float(time.time())
print("Execution time")
print(str(float(end - start)) + str("s"))
Best['SelectionSort'] = str(float(end - start))

# Call for def BubbleSort:
print("Bubble Sort :")
arr = random.sample(range(1, length+1), length)
print("Length of array is " + str(len(arr)))
print("Actual Array :")
print(arr)
start = float(time.time())
print("Sorted Array :")
print(BubbleSort.BubbleSort(arr))           
end = float(time.time())
print("Execution time")
print(str(float(end - start)) + str("s"))
Best['BubbleSort'] = str(float(end - start))

# Call for def QuickSort:
print("Quick Sort :")
arr = random.sample(range(1, length+1), length)
print("Length of array is " + str(len(arr)))
print("Actual Array :")
print(arr)
low = 0
high = len(arr)-1
start = float(time.time())
print("Sorted Array :")
print(QuickSort.QuickSort(arr,low,high))           
end = float(time.time())
print("Execution time")
print(str(float(end - start)) + str("s"))
Best['QuickSort'] = str(float(end - start))

# Call for def QuickSort Three Median:
print("Quick Sort using 3 Medians :")
arr = random.sample(range(1, length+1), length)
print("Length of array is " + str(len(arr)))
print("Actual Array :")
print(arr)
low = 0
high = len(arr)
start = float(time.time())
print("Sorted Array :")
print(QuickSortTM.QuickSort(arr, low, high))           
end = float(time.time())
print("Execution time")
print(str(float(end - start)) + str("s"))
Best['QuickSortThreeMed'] = str(float(end - start))

#Choose the best algorithm based on input
print("Algorithms and their execution time")
print(Best)
lowest = min(Best.values())
# print(min(Best.values()))
print(lowest)

for key, value in Best.items():
         if lowest == value:
             print("Best Algorithm is :" + key + " with execution time :" + lowest + "s")
             