from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_indices = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i
    
    return []

if __name__ == "__main__":
    user_input = input("Enter a list of numbers separated by spaces: ")
    nums = list(map(int, user_input.split()))
    target = int(input("Enter the target sum: "))
    result = twoSum(nums, target)
    print("Indices of the numbers that add up to the target:", result)
