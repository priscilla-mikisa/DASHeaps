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

"""Given a stream of integers and a number k, 
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



"""You have a collection of stones, each stone has a positive integer weight.
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




