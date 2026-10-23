from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        while queue:
            curr = queue.popleft()
            for c in graph[curr]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    queue.append(c)
        return sum(indegree) == 0