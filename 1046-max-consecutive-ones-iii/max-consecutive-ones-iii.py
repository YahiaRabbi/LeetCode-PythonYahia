class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_window = 0
        zeros = 0
        left = 0

        for right in range(n):          #counting total zeros
            if nums[right] == 0:
                zeros += 1
            
            while zeros > k:            #flipping(invalid window)
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            windows = right - left + 1   #valid window
            max_window = max(max_window, windows)

        return max_window
