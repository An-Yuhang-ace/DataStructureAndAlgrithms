# https://leetcode.cn/problems/3sum/

def twoSum(nums, target):
    res = []
    left, right = 0, len(nums)-1
    while left < right:
        sum = nums[left] + nums[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            res.append([nums[left], nums[right]])
            left += 1
            while left < len(nums) and nums[left] == nums[left-1]:
                left += 1
            right -= 1
            while right >= 0 and nums[right] == nums[right+1]:
                right -= 1
    return res

def threeSum(nums):
    ans = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -1 * nums[i]
        res = twoSum(nums[i+1:], target)
        if len(res) != 0:
            for j in range(len(res)):
                res[j].append(nums[i])
                ans.append(res[j])
    return ans

if __name__ == "__main__":
    nums = [-2,0,0,2,2]
    print(threeSum(nums))