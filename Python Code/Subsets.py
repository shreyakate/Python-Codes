class Solution(object):
    res = []
    def genSets(self,curr,nums):
        if curr not in self.res:
            self.res.append(curr) 
        if nums:
            self.genSets(curr,nums[1:])
            self.genSets(curr+[nums[0]],nums[1:]) 
        else:
            return
        
    def subsets(self, nums):
        self.res =[]
        nums.sort()
        self.genSets([],nums)
        return self.res

s = Solution()
print s.subsets([4,4,4,1,4])
StringManSMS("Hello World this is Shreya",10)

def StringManSMS(str, n):
    words= str.split()
    res = ''
    tmp = ''
    i = 0
    while words:
        if len(words[i])> n:
            tmp = words[i][:n+1]
            carry = words[i][n+1:]

