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






