class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left=0
        visit=set()
        maxlen=0

        for right in range(len(s)):
            while s[right] in visit:
                visit.remove(s[left])
                left+=1

            visit.add(s[right])
            maxlen=max(maxlen,right-left+1)

        return maxlen


