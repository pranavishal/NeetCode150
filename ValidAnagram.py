class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 
        
        sMap = {}
        tMap = {}

        for i in range(len(s)):
            if s[i] not in sMap:
                sMap[s[i]] = 1
            else:
                sMap[s[i]] += 1
            
            if t[i] not in tMap:
                tMap[t[i]] = 1
            else:
                tMap[t[i]] += 1

        for key, value in sMap.items():
            if key not in tMap:
                return False
            
            if sMap[key] != tMap[key]:
                return False
        
        return True

        
