# https://leetcode.cn/problems/two-sum/

def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        m = target - nums[i]
        if m not in dict:
            dict[nums[i]] = i
        else:
            return [dict[m], i]
    return []

if __name__ == "__main__":
    nums = [3, 2]
    target = 5

    print(twoSum(nums, target))
