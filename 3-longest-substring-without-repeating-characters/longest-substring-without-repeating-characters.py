class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        st = set()

        for right in range(len(s)):
            while s[right] in st:       #invalid window
                st.remove(s[left])
                left += 1

            w = (right - left) + 1
            longest = max(longest, w)
            st.add(s[right])           #adding new elem for valid window

        return longest                  #time: O(n)
