class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        flag = 0
        twoZero = 0
        producthelper1=1
        producthelper2=1
        products = []
        for i in range(len(nums)):
            if nums[i]==0:
                flag=i
                products1=[]
                for j in range(len(nums)):
                    if nums[j]!=0:
                        producthelper1*=nums[j]
                        products1.append(0)
                    elif nums[j]==0:
                        twoZero +=1
                        products1.append(0)
                if twoZero<=1:
                    products1[flag]=producthelper1
                return products1
            producthelper2*=nums[i]
        for i in range(len(nums)):
            products.append(producthelper2//nums[i])
        return products

                        

        