class Solution:
    def containsCheck(self, s: str, t: str) -> bool:
        tMap = {}
        sMap = {}

        for j in t:
            if j not in tMap:
                tMap[j] = 1
            else:
                tMap[j] += 1
        
        for i in s:
            if i not in sMap:
                sMap[i] = 1
            else:
                sMap[i] += 1
        
        for key, value in tMap.items():
            if key not in sMap:
                return False
            
            elif value > sMap[key]:
                return False
            
        return True

    def minWindow(self, s: str, t: str) -> str:
        # Step 1.
        # Start with the sliding window starting at the beginning of s, and the ending of
        # the window expanding until s contains all letters of T

        # Step 2.
        # From there, move the beginning of the window forward, and stopping if s no longer 
        # contains all characters of T 

        # Step 3.
        # Then, the window becomes fixed and we slide it over by 1. 

        # Step 4.
        # If the window still contains all of t, we then check to see if we 
        # can move the beginning further to shrink the window while containing all of t

        # Step 5.
        # Once we can no longer shrink the window, we repeat steps 3 and 4 until we iterate
        # until the end of the array

        
        # Step 1.
        contains = True
        begin = 0
        end = 1

        for i in range(len(s)):
            contains = self.containsCheck(s[begin:end], t)
            
            if contains:
                break
            else:
                end += 1
        

        # Step 2.
        print(s[begin:end])
        if not contains:
            return ""
        
        #return ""
        
        contains = True
        for i in range(end + 1):
            contains = self.containsCheck(s[i:end], t)
            if not contains:
                begin = i - 1
                break
        
        print(s[begin:end])

        #return "LOL"

        #step 3

        #we need to store the smallest substring of s
        substring = s[begin:end]

        while end < len(s):
            end += 1
            begin += 1
            contains = self.containsCheck(s[begin:end], t)
            
            if not contains:
                continue
            
            #step 4
            else:
                while contains:
                    #Here we move begin as much as we can
                    contains = self.containsCheck(s[begin + 1:end], t)
                        
                    if contains:
                        begin += 1
                        substring = s[begin:end]

        return substring

                




            



            



        
