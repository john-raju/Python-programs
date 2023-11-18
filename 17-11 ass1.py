class Solution:
    def kLargest(self,li,n,k):
        li.sort(reverse=True)
        return li[:k]
