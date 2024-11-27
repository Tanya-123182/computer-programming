#Merge k Sorted Lists

import heapq
def merge_k_sorted_lists(lists):
    min_heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))
    result = []
    while min_heap:
        val, list_idx, elem_idx
