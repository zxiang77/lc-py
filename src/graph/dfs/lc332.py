from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # dfs with ordering
        if not tickets or len(tickets) == 0:
            return []
        total = len(tickets)
        m4p = {}
        for (src, dst) in tickets:
            if src not in m4p.keys():
                m4p[src] = []
            m4p[src].append(dst)

        for k in m4p.keys():
            m4p[k].sort()

            m4p[k] = list(map(lambda i: [i, False], m4p[k]))  # sort and have a key to record if used

        path = ['JFK']

        def helper(stp):  # the first found is guarenteed to be the shortest path
            nonlocal total
            src = path[-1]
            if stp == total:
                return True  # found
            # i don't want to search on the same dest twice with the same origin
            used = set()

            for record in m4p.get(src, []):
                if (not record[1]) and (record[0] not in used):
                    used.add(record[0])
                    path.append(record[0])
                    record[1] = True
                    if helper(stp + 1):
                        return True
                    record[1] = False
                    path.pop()
            return False

        helper(0)
        return path

# print((Solution()).findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
