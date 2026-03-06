1class Solution:
2    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        index1 = {n:i for i, n in enumerate(nums1)}
4        res = [-1] * len(nums1)
5        stack = []
6
7        for i in range(len(nums2)):
8            while (stack and nums2[i] > stack[-1]):
9                val = stack.pop()
10                index = index1[val]
11                res[index] = nums2[i]
12            if nums2[i] in index1:
13                stack.append(nums2[i])
14        return res