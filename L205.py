class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict={}
        if not s:
            return True
        for i in range(len(s)):
            if s[i] not in dict:
                if t[i]  in dict.values():
                    print(i)
                    return False
                else:
                    dict[s[i]]=t[i]
            else:
                if dict[s[i]]!=t[i]:
                    print(i)
                    return False
        return True

