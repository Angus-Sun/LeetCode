class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(arr,k):
            larger = []
            smaller = []
            equal = 0
            pivot = random.choice(arr)
            for num in arr:
                if num > pivot:
                    larger.append(num)
                elif num < pivot:
                    smaller.append(num)
                else:
                    equal += 1
            if k <= len(smaller):
                return quickSelect(smaller, k)
            elif k > len(smaller) + equal:
                return quickSelect(larger, k-len(smaller)-equal)
            else:
                return pivot
        return quickSelect(nums, len(nums)-k+1)

             