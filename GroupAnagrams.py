class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        anagramList = []
        
        for string in strs:
            strDict = {}
            for char in string:
                if char not in strDict:
                    strDict[char] = 1
                else:
                    strDict[char] += 1
            
            listKey = []
            
            for letter in range(ord('a'), ord('z') + 1):
                if chr(letter) not in strDict:
                    listKey.append(0)
                else:
                    listKey.append(strDict[chr(letter)])
            
            tupleKey = tuple(listKey)

            if tupleKey not in anagramDict:
                anagramDict[tupleKey] = [string]
            else:
                anagramDict[tupleKey].append(string)
        
        for key, value in anagramDict.items():
            anagramList.append(value)
        
        return anagramList




            
                

