class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) ==1:
        #     return 0
        # if len(nums) ==2:
        #     if nums[0]>nums[1]:
        #         return 0
        #     else:
        #         return 1
        # for i in range(1, len(nums)-1):
        #     if (nums[i-1]< nums[i]) and (nums[i]>nums[i+1]):
        #         return i
        #     if nums[0]>nums[1]:
        #         return 0
        #     if nums[len(nums)-1]>nums[len(nums)-2]:
        #         return (len(nums)-1)
        
        # #sol 2
        # for i in range(len(nums)-1):
        #     if nums[i]>nums[i+1]:
        #         return i
        # return len(nums)-1
        
#         # sol: binary search
#         n = len(nums)
#         return self.search(nums, 0, (n-1))
    
#     def search(self, nums, left, right):
#         if left == right:
#             return left
#         mid = int((left+right)/2)
#         # print(mid)
#         if nums[mid] > nums[mid +1]:
#             return self.search(nums, left, mid)
#         return self.search(nums, mid+1, right)

    #Sol: iterative binary search
        left = 0
        right = len(nums)-1
        
        while(left<right):
            mid = int((left+right)/2)
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left

                
            
            
