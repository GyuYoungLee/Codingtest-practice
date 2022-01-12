def two_sum(nums, target):
    d = {}

    for i, x in enumerate(nums):
        c = target - x
        if c in d:
            return i, d[c]
        d[x] = i

    return False


print(two_sum([2, 7, 9, 15], 9))
print(two_sum([3, 3], 6))
print(two_sum([1, 3], 2))
