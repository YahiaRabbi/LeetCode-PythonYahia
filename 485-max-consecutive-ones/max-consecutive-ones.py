class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        x = len(nums)

        for i in range(1,x):
            if nums[i]:
                nums[i] += nums[i-1]

        return max(nums)
        """

        maxx = 0
        current = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
                if current > maxx:
                    maxx = current
            else:
                current = 0

        return maxx