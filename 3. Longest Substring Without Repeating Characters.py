class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        start = 0
        curMax = 0
        used_dict = {}
        for n, char in enumerate(s):
            if (char in used_dict) and (used_dict[char] >= start):  # new char
                start = used_dict[char] + 1  # new start
                used_dict[char] = n  # new to dict
                # if n >= 1 and s[n] == s[n - 1]:
                #     start -= 1
            else:  # in used list
                used_dict[char] = n  # add to dict
                # print('curr max', curMax, 'new max', n - start + 1)
                curMax = max(curMax, n - start + 1)  # new count

            # print('_____________________curr max', curMax, 'new max', n - start + 1)
            # print('start:',s[start], start, '\n')
        return curMax
