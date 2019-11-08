def build_order(numCourses, prerequisites):
        projects = list(range(numCourses))
        map_dependant = dict()
        # projects that each project is dependant on
        for p in projects:
            map_dependant[p] = set()
        for pa in prerequisites:
            map_dependant[pa[1]].add(pa[0])

        # map_dependancy = dict() # dictionary containing the projects each project is dependant on
        # for p in projects:
        #     map_dependancy[p] = set()
        # for pa in prerequisites:
        #     map_dependancy[pa[0]].add(pa[1])

        completed = set()
        order = list()
        queue = list()
        queue_set = set()
        visited = set()

        for project, dependencies in map_dependant.items():
            if not dependencies:
                completed.add(project)
                order.append(project)
        for p in projects:
            if p in completed:
                continue
            visited = completed.copy()
            print(visited)
            queue.append(p)
            while queue:
                cur = queue[0]
                del queue[0]
                visited.add(cur)
                if map_dependant[cur].issubset(completed):
                    completed.add(cur)
                    order.append(cur)
                    for p in map_dependant[cur]:
                        if p not in visited:
                            visited.add(p)
                            queue.append(p)
        print(order)
        ret = True if len(order) == numCourses else False
        return ret

print(build_order(9, [[1,2], [2,3], [3,4], [0,5], [0,6], [7,8], [8,1]]))
