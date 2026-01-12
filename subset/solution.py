def backtrack(index, current, result, nums):
    # If we've considered all elements, add the subset
    if index == len(nums):
        result.append(current[:])  # make a copy
        return

    # Choice 1: exclude nums[index]
    backtrack(index + 1, current, result, nums)

    # Choice 2: include nums[index]
    current.append(nums[index])
    backtrack(index + 1, current, result, nums)
    current.pop()  # undo the choice

def find_all_subsets(nums):
    """
    Returns all possible subsets (the power set) of the given list of integers.

    The order of subsets may vary.

    >>> find_all_subsets([])
    [[]]

    >>> sorted(find_all_subsets([1]))
    [[], [1]]

    >>> sorted(find_all_subsets([1, 2]))
    [[], [1], [1, 2], [2]]

    >>> sorted(find_all_subsets([1, 2, 3]))
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    """
    result = []
    backtrack(0, [], result, nums)
    return result
