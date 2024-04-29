class Solution(object):
    def countStudents(self, students, sandwiches):
        current_length = len(students)
        current_sandwich = sandwiches.pop(0)

        while(current_length>0):
            current_student = students.pop(0)
            #Only if the current sandwich and current student matches then pop another sandwich and update current length
            if current_sandwich == current_student:
                if(len(sandwiches)>0):
                    current_sandwich = sandwiches.pop(0) #Not to pop for the last time as there will be an index error
                current_length=len(students)
                continue
            else:
                students.append(current_student)
            current_length-=1   
        return len(students)
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """