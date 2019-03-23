# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort( key = lambda x: x.start)
        
        heap = []
        for i in intervals:
            if heap and i.start>=heap[0]:
                heap[0] = i.end
                # heapq.heapreplace(heap, i.end)
            else:
                heap.append(i.end)
                # heapq.heappush(heap, i.end)
            heap.sort()
        return len(heap)
        
        
#         intervals.sort( key = lambda x: x.start)
        
#         heap = []
#         for i in intervals:
            
#             if heap and i.start>=heap[0]:  #can use the same room 
#                 print('i.start:',i.start)
#                 print('heap 0:', heap[0])
#                 print(heap)
#                 heapq.heapreplace(heap, i.end) 
#             else:    #have a new room
#                 heapq.heappush(heap, i.end) 
        
#         return len(heap)
        
        
        
        
        
        
        
        
        
        
        
        
#         intervals.sort(key = lambda x: x.start)
#         heap = []
        
#         for i in intervals:
#             if heap and (heap[0] <= i.start):
#                 #  the direct implementation would be keep a heap to store every room's latest event ending time.
#                 heapq.heapreplace(heap, i.end)
#             else:
#                 heapq.heappush(heap, i.end)
            
#         return len(heap)

        
    
    
    
                    
            
