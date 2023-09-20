# https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof/

def twoSum(nums, target):
    left, right = 0, len(nums)-1
    while left < right:
        sum = nums[left] + nums[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            return [nums[left], nums[right]]
    return []

if __name__ == "__main__":
    nums = [10,26,30,31,47,60]
    target = 40
    print(twoSum(nums, target))