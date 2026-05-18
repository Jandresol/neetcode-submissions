class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs topological sort (cycle detection)
        # create a hashmap that maps each course
        # to its prerequisits
        hashmap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            hashmap[course].append(pre)
        
        # courses in the current path
        visiting = set()

        # dfs every course
        def dfs(course):
        # if we visited a prereq
            if course in visiting:
                return False
            if hashmap[course] == []:
                return True
            # this is in the path
            visiting.add(course)
            # look at its prereq
            for prereq in hashmap[course]:
                # if cycle in the prereq
                if not dfs(prereq):
                    return False
            # once we're done we got it!
            visiting.remove(course)
            hashmap[course] = []
            return True
        
        # make sure the graph has absolutely no cycles
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

        