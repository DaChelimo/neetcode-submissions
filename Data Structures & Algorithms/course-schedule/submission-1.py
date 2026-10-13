from collections import defaultdict

class Solution:
    # Create a adjacency list
    # Start at 0 with prerec 1, and follow children
    # Once you finish dfs-ing, check if the visited nodes are equal to the num of courses
    # Time: O(m + n). Space: O(m + n)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPreRec = defaultdict(list)
        
        for prerec in prerequisites:
            course = prerec[0]
            preCourse = prerec[1]

            courseToPreRec[course].append(preCourse)

        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            if courseToPreRec[course] == []:
                return True
            
            visited.add(course)

            for pre in courseToPreRec[course]:
                if not dfs(pre): 
                    return False

            visited.remove(course)
            courseToPreRec[course] = []
            
            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True


