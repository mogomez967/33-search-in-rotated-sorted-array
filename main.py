def search(nums, target):
    result = -1
    if target not in nums:
        return result
    else:
        # I now know that the num is in the array.
        # The array is sorted but possibly in a weird order.
        # I must return the position of the given input "target"
        # algorithm:
        #     index_of(target(in list nums))
        # this is the trivial method using given python functions
        result = nums.index(target)
    return result

nums = [4, 5, 6, 7, 0, 1, 2]
target = 1
print(search(nums, target))