from collections import defaultdict


class Course:
    def __init__(self):
        self.num_of_prerequisites = 0
        self.prerequisite_for = set()
    def course_completed(self):
        return self.num_of_prerequisites == 0
    def add_prerequisite_for(self, other_course):
        self.prerequisite_for.add(other_course)
    def increment_prerequisites(self):
        self.num_of_prerequisites += 1
    def defcrement_prerequisites(self):
        self.num_of_prerequisites -= 1
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        g = defaultdict(Course)
        for src, dst in prerequisites:
            g[dst].add_prerequisite_for(src)
            g[src].increment_prerequisites()
        stack = [k for k in g if g[k].course_completed()]
        while stack:
            curr = stack.pop()
            for n in g[curr].prerequisite_for:
                g[n].defcrement_prerequisites()
                if g[n].course_completed():
                    stack.append(n)
        for course in g.values():
            if not course.course_completed():
                return False
        return True