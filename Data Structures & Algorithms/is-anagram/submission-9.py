class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}
        for l in s:
            if l in hash1:
                hash1 [l] += 1
            else:
             hash1 [l] = 1
        for l in t:
            if l in hash2:
                hash2 [l] += 1
            else:
                hash2 [l] = 1

        if hash1 == hash2:
            return True
        return False

                 
            
            





        '''
        hash1 = set(s)
        hash2 = set(t)
        if len(s) == len(t):
            if hash1 == hash2:
             return True
        return False 
        '''


