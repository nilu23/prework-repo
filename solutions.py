

#################################
# Level - 1
################################
"""
What is the time complexity of the following code :

        int j = 0;
        for(i = 0; i < n; ++i) {
            while(j < n && arr[i] < arr[j]) {
                j++;
            }
        }

Answer - O(n)

"""

#################################
# Level - 2 - PRETTYPRINT
################################
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        i, res = 2, [[1]]
        while i <= A:
            for j in range((i-1)*2-1):
                res[j] = [i] + res[j] + [i]
            res.insert(0, [i] *(i*2-1))
            res.append([i]*(i*2-1))
            i += 1
        return res


#######################################################
# Level - 3 - Kth Smallest Element in the Array
######################################################
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        if B:
            return sorted(A)[B-1]
        else:
            return
    import random

    def ksmallest_2(nums,k):
        lo, hi, w = 0, len(nums)-1,0
        while(lo<=hi):
            p=random.randint(lo,hi)
            pivot=nums[p]
            nums[p],nums[hi]=nums[hi],nums[p]
            w=lo
            for u in range(lo,hi):
                if(nums[u]>pivot):
                    nums[u],nums[w]=nums[w],nums[u]
                    w+=1
            nums[hi],nums[w]=nums[w],nums[hi]
            if(w>hi-k+1):
                k=k-(hi-w+1)
                hi=w-1
            elif(w<hi-k+1):
                lo=w+1
            else:
                return nums[w]
        return nums[w]

#######################################################
# Level - 4 - NEXTGREATER
######################################################
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):

        res =[]
        for i in range(0, len(A), 1):
            next = -1
            for j in range(i+1, len(A), 1):
                if A[i] < A[j]:
                    next = A[j]
                    break
            res.append(next)
        return res

#######################################################
# Level - 5 - Longest Consecutive Sequence
######################################################
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        longest_streak = 0
        num_set = set(A)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
