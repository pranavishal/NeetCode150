class Solution:

    def encode(self, strs: List[str]) -> str:
        decodedString = ""

        for string in strs:
            length = str(len(string)) + "#"
            decodedString += length + string
        
        print(decodedString)
        return decodedString


    def decode(self, s: str) -> List[str]:
        
        stringList = []
        currentString = ""
        inWord = False
        lengthRemainingInWord = 0
        currentWordLength = ""
        for char in s:
            if char.isdigit() and not inWord:
                currentWordLength += char
                
            elif char == "#" and not inWord:
                try:
                    lengthRemainingInWord = int(currentWordLength)
                except:
                    print(currentWordLength)

                inWord = True
                currentWordLength = ""

                if lengthRemainingInWord == 0:
                    inWord = False
                    currentWordLength = ""
                    stringList.append("")
            
            else:

                if inWord and lengthRemainingInWord == 1:
                    inWord = False
                    currentString += char
                    lengthRemainingInWord -= 1
                    stringList.append(currentString)
                    currentString = ""

                elif inWord and lengthRemainingInWord > 0:
                    currentString += char
                    lengthRemainingInWord -= 1
                
        
        return stringList



            




