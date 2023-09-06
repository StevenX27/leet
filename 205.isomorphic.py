class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_count = {}
        t_count = {}
        
        for i,letter in enumerate(s):
            
            s_count.setdefault(letter,[]).append(i)
        for i,letter in enumerate(t):
            
            t_count.setdefault(letter,[]).append(i)
        
        return sorted(list(t_count.values())) == sorted(list(s_count.values()))

sol = Solution()
sol.isIsomorphic( "egg", "add")