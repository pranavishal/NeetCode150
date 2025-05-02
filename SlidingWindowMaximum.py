import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        returnList = []

        heap = []

        windowStart = 0
        windowEnd = k - 1

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        
        print(heap)
        

        returnList.append(heap[0][0] * -1)

        windowStart = 1
        windowEnd = k

        while windowEnd < len(nums):
            heapq.heappush(heap, (-nums[windowEnd], windowEnd))

            while True:
                print(heap)
                windowMax = heap[0]
                if windowMax[1] >= windowStart and windowMax[1] <= windowEnd:
                    break
                else:
                    heapq.heappop(heap)

            returnList.append(windowMax[0] * -1)
            windowStart += 1
            windowEnd += 1
                    

        return returnList



        
