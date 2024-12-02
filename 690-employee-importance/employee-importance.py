"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # importance=0
        # queue=set({id})
        # new_list = sorted(employees, key=lambda x: x.id, reverse=False)
        # # print(employees)
        # for employee in new_list:
        #     # print(employee.id)
        #     if employee.id in queue:
        #         for cur_id in employee.subordinates:
        #             queue.add(cur_id)
        #         # print(queue,employee.id)
        #         importance+=employee.importance
        #         # queue.pop(0)

        # # print(queue,importance)
        # # print(queue)
        # return importance

        def dfs(id: int) -> int:
            e = map[id]
            sum = e.importance
            for sub_id in e.subordinates:
                sum += dfs(sub_id)
            return sum
        
        map = {}
        for e in employees:
            map[e.id] = e
        
        return dfs(id)