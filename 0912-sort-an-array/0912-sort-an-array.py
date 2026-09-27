class Solution:

    # merge sort
    def merge(self, nums, l, mid, r):
        a = []
        b = []

        for i in range(l,mid+1):
            a.append(nums[i])
        for i in range(mid+1, r+1):
            b.append(nums[i])

        i,j,k=0,0,l

        while k<=r:
            if j==len(b):
                nums[k] = a[i]
                i+=1
                k+=1
            elif i == len(a):
                nums[k] = b[j]
                j+=1
                k+=1

            elif a[i] < b[j]:
                nums[k] = a[i]
                i+=1
                k+=1
            else:
                nums[k] = b[j]
                j+=1
                k+=1

    def mergeSort(self, nums, l, r):
        # base case
        if l>=r:
            return
        
        # (repete) recursive case
        mid= (l+r)//2
        self.mergeSort(nums,l,mid)
        self.mergeSort(nums,mid+1,r)

        self.merge(nums,l,mid,r)


    def sortArray(self, nums: list[int]) -> list[int]:
        self.mergeSort(nums,0,len(nums)-1)
        return nums
  
        # nums.sort()
        # return nums

 # bubble sort.......... 
        # n = len(nums)

        # for i in range(n):
        #     isSwap = False
        #     for j in range(n-i-1):
        #         if nums[j]>nums[j+1]:
        #             temp = nums[j]
        #             nums[j] = nums[j+1]
        #             nums[j+1] = temp
        #             isSwap = True
        #     if not isSwap:
        #         break
        # return nums


        # insertion sort .............
        # n = len(nums)
        # for i in range(1,n):
        #     key = nums[i]
        #     j = i-1
        #     while j>=0 and nums[j]>key:
        #         nums[j+1] =nums[j]
        #         j-=1
        #     nums[j+1] = key
        # return nums




        # selection sort..........
        # n = len(nums)

        # for i in range(n):
        #     mn = nums[i]
        #     ind = i
        #     for j in range(i+1, n):
        #         if nums[j]<mn:
        #             mn = nums[j]
        #             ind = j
        #     temp = nums[i]
        #     nums[i] = nums[ind]
        #     nums[ind] = temp
        # return nums

        