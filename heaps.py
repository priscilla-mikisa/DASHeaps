import heapq
def create_max_heap(arr):
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)
    return max_heap
def access_element(heap, index):
    return -heap[index]
def delete_element(heap, element):
    try:
        element = -element
        index = heap.index(element)
        heap[index] = heap[-1]
        heap.pop()
        heapq.heapify(heap)
        return True
    except ValueError:
        return False
arr = [20, 15, 10, 8, 9, 7, 5]
heap = create_max_heap(arr)
print("Max-Heap:", [-x for x in heap])
index_to_access = 2
print(f"Element at index {index_to_access}: {access_element(heap, index_to_access)}")
element_to_delete = 10
success = delete_element(heap, element_to_delete)
if success:
    print(f"Element {element_to_delete} deleted successfully.")
else:
    print(f"Element {element_to_delete} not found.")
print("Heap after deletion:", [-x for x in heap])






"""Interview Questions"""

"""1. Given a stream of integers and a number k, 
design a data structure that can find the kth largest element in the stream.?"""


"""Assuming the stream is an array, using heaps other than lists will be suitable to arrnge 
because it requires a less time complexity of O(nlogn) time"""
"""In the code below, Time complexity: O(N * log(N)) and Space: O(1) """

"""Create a function called klargest that takes in an array and a variable "k" as the Nth number"""
def kLargest(arr, k):
    """We sort the array in reverse order to get the largest as the last element"""
    arr.sort(reverse=True)
    """When sortting, the reverse is true so that we specify the numbers arragement in ascending order"""
    for i in range(k):
        
        print(arr[i], end="")
"""Specify the array"""
arr = [1, 23,50, 12, 9, 30, 2]
"""Print the first "kth" element"""
k=1
print(kLargest(arr,k))

                                        

"""2. You have a collection of stones, each stone has a positive integer weight.
Each turn, you choose the two heaviest stones and smash them together.
Imagine that after each such turn, the remaining stones are piled together.
After each turn, you choose the two heaviest remaining stones.
If a stone of weight x meets a stone of weight y, the resulting stone
will have weight x-y. How many turns will it take to reduce the collection to at
most 1 stone?"""

"Pseudo Code"
"1. Create an array of the stones with the different weights"
"2. Organise the stones in descending order to get the first two as the biggest stones"
"3. Smash the stones to get the new generated stone that has a weight which is the difference of the two parent stones"
"4. Repeat the process from step1 to step3 until only one stone remains"
"5. Display the weight of the last stone."

def last_stone_weight(stones):
    "We turn the array into a max heap because it will organise the tree from the largest number and the child nodes will be smaller than the parent nodes"
    "This will help us to sort easily with a small time complexity"
    max_heap = [-stone for stone in stones]
    heapq.heapify(max_heap)
    
    while len(max_heap)>1:
        stone1 = -heapq.heappop(max_heap)
        stone2 = -heapq.heappop(max_heap)
        
        if stone1 != stone2:
            new_stone = abs(stone1-stone2)
            heapq.heappush(max_heap, -new_stone)
    return -max_heap[0] if max_heap else 0
stones = [2,7,4,9,80,5]
results = last_stone_weight(stones)
print("The weight of the last remaining stone is:", results)


"""3. Given a matrix mat where every row is sorted in non-decreasing order and the first integer of each
row is greater than the last integer of the previous row. Provided also is an integer k. The task is to
output the k weakest rows in the matrix, in decreasing order of strength."""

"Pseudo Code"
"""1. Create a function that will take in two arguments. The
first argument the matrix and the other argument the k-number 
of elements to return.
"""
"""2. Initialize an empty heap to store the tuples having both the index and the total of the elements."""
"""Loop through the rows to get teir sum and index of eeach row"""
"""Find the sum and index of each row in the matrix."""
"""Put the reesults in a new list in ascending order"""
"""Display the "k" elements from the arranged list."""


from heapq import heappush, heappop

def kWeakestRows(mat, k):
    heap = []
    for i, row in enumerate(mat):
        positives = sum(row)
        heappush(heap, (positives, i))
    
    results = []
    for _ in range(k):
        results.append(heappop(heap)[1])
    
    return results

mat = [[1, 1, 0, 0, 0],
       [0, 0, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0]]
k = 2

result = kWeakestRows(mat, k)
print(result)

"""4. Find the kth largest element in an unsorted array. 
Note that it is the kth largest element in the sorted order,
not the kth distinct element.
"""

"Pseudo Code"
"1. Create a function that will take in both the  list of numbers and the of 'k' position. "
"2. Add the first k ele,ents to a list."
"3. Transform the list to a heap."
"4. Create a cretaria for adding the numbers from the list in a particular order. ie. only add the number if the current number is larger than the smallest heap."
"5. Remove the smallest elements to only remain with the largest elements."
"6. display the largest element."

import heapq

def findKthLargest(nums, k):
    " Create a min-heap with the first k elements"
    min_heap = nums[:k]
    
    "Transform the list into a heap in O(k) time"
    heapq.heapify(min_heap) 
    "Process the remaining elements"
    for num in nums[k:]:
        "Only add to heap if the current number is larger than the smallest in the heap"
        if num > min_heap[0]:
            "Remove the smallest element"  
            heapq.heappop(min_heap) 
            "Add the current number"
            heapq.heappush(min_heap, num)

    "The root of the min-heap is the kth largest element"
    return min_heap[0]


nums = [7, 10, 4, 3, 20, 15]
k = 3
result = findKthLargest(nums, k)
print(result) 

"""5. Design a data structure that supports the
following operations: add a number and find the median. """
import heapq

class MedianFinder:
    def __init__(self):
        "Max heap for the lower half (inverted to use Python's min-heap)"
        self.max_heap = []
        "Min heap for the upper half"
        self.min_heap = []

    def addNum(self, num: int) -> None:
        "Add to max heap (lower half)"
        heapq.heappush(self.max_heap, -num)

        "Ensure the largest of the lower half is less than or equal to the smallest of the upper half"
        if (self.max_heap and self.min_heap and 
            (-self.max_heap[0] > self.min_heap[0])):
            "Move the largest from max_heap to min_heap"
            value = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, value)

        "Balance the sizes of the heaps"
        if len(self.max_heap) > len(self.min_heap) + 1:
            "Move the largest from max_heap to min_heap"
            value = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, value)
        elif len(self.min_heap) > len(self.max_heap):
            "Move the smallest from min_heap to max_heap"
            value = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -value)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            "If max_heap has more elements, the median is the root of max_heap"
            return float(-self.max_heap[0])
        else:
            "If both heaps are of equal size, the median is the average of the roots"
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0

medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())
medianFinder.addNum(3)
print(medianFinder.findMedian()) 

            

   




