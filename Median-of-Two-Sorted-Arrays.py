1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        A, B = nums1, nums2
4        if len(B) < len(A):
5            A,B = B,A
6        total = len(nums1) + len(nums2)
7        half = total // 2
8        l, r = 0, len(A)-1
9        while True:
10            midA = (l + r) // 2
11            midB = half - midA - 2
12
13            leftA = A[midA] if midA >= 0 else float("-infinity")
14            rightA = A[midA+1] if midA+1 < len(A) else float("infinity")
15            leftB = B[midB] if midB >= 0 else float("-infinity")
16            rightB = B[midB+1] if midB+1 < len(B) else float("infinity")
17
18            if leftA <= rightB and leftB <= rightA:
19                if total % 2:
20                    return min(rightA, rightB)
21                return (max(leftA, leftB) + min(rightA, rightB)) / 2
22            elif leftA > rightB:
23                r = midA - 1
24            else:
25                l = midA + 1
26