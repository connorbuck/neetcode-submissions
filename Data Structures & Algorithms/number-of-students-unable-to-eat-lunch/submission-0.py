from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_queue = deque(students)
        sandwich_queue = deque(sandwiches)

        num_skipped = 0
        while num_skipped != len(student_queue) and len(student_queue) != 0:
            first_student = student_queue.popleft()
            if first_student == sandwich_queue[0]:
                sandwich_queue.popleft()
                num_skipped = 0
                continue
            
            student_queue.append(first_student)
            num_skipped += 1
        
        return len(student_queue)