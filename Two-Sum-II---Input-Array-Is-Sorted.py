1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        i,j = 0, len(numbers)-1
4        while (numbers[i]+numbers[j] != target):
5            if numbers[i]+numbers[j] > target:
6                j-=1
7            else:
8                i+=1
9        return [i+1, j+1]