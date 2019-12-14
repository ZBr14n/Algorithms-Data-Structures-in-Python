"""
 
"""
def maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4]):
    
    Sum=0
    store=[]
    for i in range(len(nums)-1):
        Sum = nums[i]+nums[i+1]
        while nums[i] > Sum and Sum >= 0:
            store.append(nums[i])
        