from heapq import heappush, heappop


def topK(arr, k):
    heap = []
    if not arr:
        return heap

    heap_set = set()
    for item in arr:
        if item in heap_set:
            continue
        if len(heap) < k:
            heappush(heap, item)
            heap_set.add(item)
        else:
            if item > heap[0]:
                out = heappop(heap)
                heap_set.remove(out)
                heappush(heap, item)
                heap_set.add(item)
    return heap


print(topK([1, 2, 3, -1, 5, 6], 3))
