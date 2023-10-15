class Solution:
    def twoSum(self, nums, target):
        dict_check = {}

        for cnt, num in enumerate(nums):
            if target - num in dict_check:
                return dict_check[target - num], cnt
            dict_check[num] = cnt


nums = [2, 7, 11, 15]
target = 9
Sol = Solution()
answer = Sol.twoSum(nums, target)
print(answer)
