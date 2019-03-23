class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #build two dict
        # freq is the dict for every number; tail is the tail's continuous seq numbers
        freq = collections.Counter(nums)
        tail = collections.Counter()
        
        for i in nums:
            if freq[i] ==0:  # indicate that new seq has been set on last round, so just skip to the next number
                continue

            freq[i] -= 1    #indicate i has been scanned
            
            if tail[i-1]>0:  #exists the last number's seq
                tail[i-1] -= 1    
                tail[i] += 1      # change the i th seq
                
            elif freq[i+1]>0 and freq[i+2]>0:  #tail[i-1]==0, new a seq from i, so need to check if i+1 and i+2 exists
                freq[i+1] -= 1
                freq[i+2] -= 1
                tail[i+2] += 1
            else:
                return False
        return True
        
            
        
