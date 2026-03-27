1from collections import deque
2class Solution:
3    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
4        sq = deque(students)
5        sandwichq = deque(sandwiches)
6
7        count = 0
8        while count != len(sq)+1:
9            if not sq:
10                break
11            student = sq.popleft()
12            sandwich = sandwichq[0]
13            if sandwich != student:
14                count += 1
15                sq.append(student) 
16            else:
17                sandwichq.popleft()
18                count = 0
19        return len(sq)
20        
21