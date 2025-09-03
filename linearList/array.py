import random

# Initialization

# initial capacity of the array
array_length = 5
# create an array with initial capacity
nums: list[int] = [0] * array_length

# Random Access
def random_access(nums: list[int], index: int) -> int:
    if index > len(nums)-1 or index < 0:
        raise IndexError("Index out of bounds")
    return nums[index]
print(random_access(nums, 0))  # Output: 0

# Insertion
def insert(nums: list[int], index: int, value: int) -> list[int]:
    if index > len(nums) or index < 0:
        raise IndexError("Index out of bounds")
    for i in range(len(nums)-1, index, -1):
        nums[i] = nums[i-1]
    nums[index] = value
print(insert(nums, 1, 6))  # Output: [0, 6, 0, 0, 0]

