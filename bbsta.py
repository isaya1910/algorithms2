def GenerateBBSTArray(a):
    if len(a) == 0:
        return []
    a.sort()
    tree_size = len(a)* 2 - 1
    ans = [None] * tree_size
    generateBBSTArray(a, ans, 0, 0, len(a) - 1)
    return ans

def generateBBSTArray(initial_array, result_array, index, left, right):
    if left > right:
        return

    mid_index = left + (right - left)//2

    result_array[index] = initial_array[mid_index]

    generateBBSTArray(initial_array, result_array, index*2 + 1, left, mid_index - 1)
    generateBBSTArray(initial_array, result_array, index*2 + 2, mid_index + 1, right)

