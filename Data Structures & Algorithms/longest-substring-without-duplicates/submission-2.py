class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left = 0
        # window = set()
        # max_length = 0

        # for right in range(len(s)):
        #     while s[right] in window:
        #         window.remove(s[left])
        #         left += 1

        #     window.add(s[right])

        #     current_length = right - left + 1
        #     max_length = max(max_length, current_length)
        # return max_length

        left = 0
        last_seen = {}
        max_length = 0

        for right in range(len(s)):
            if s[right] in last_seen:
                left = max(left, last_seen[s[right]] + 1)

            last_seen[s[right]] = right

            current_length = right - left + 1
            max_length = max(max_length, current_length)

        return max_length

        