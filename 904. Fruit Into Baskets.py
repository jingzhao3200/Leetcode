class Solution:
    def totalFruit(self, tree: 'List[int]') -> 'int':
        res = 0
        nums = collections.Counter()
        l = 0
        # tree_dict = collections.Counter(tree)
        # print(tree_dict)
        for r in range(len(tree)):
            nums[tree[r]] += 1 #start to count or add count 1
            while len(nums) > 2:# if the class more than 2, keep the class to 2
                nums[tree[l]] -= 1 #find repeat, give first class -1
                if not nums[tree[l]]:
                    nums.pop(tree[l]) #get rid of 0
                l += 1 # operate for every element
            res = max(res, r - l + 1) # r-l+1 is the current length of the tree
        return res
            
    
