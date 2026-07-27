class Solution:
    def getDist(self, x, y):
        return x*x + y*y

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        heapq.heapify(maxheap)

        for p in points :
            x,y = p
            dist = self.getDist(x,y)
            t = (-dist, [x,y])
            if len(maxheap)<k:
                heapq.heappush(maxheap, t)
            elif -maxheap[0][0] > dist:
                heapq.heapreplace(maxheap, t)
        
        output = []
        for node in maxheap:
            pt = node[-1]
            output.append(pt)
        return output 
            

            