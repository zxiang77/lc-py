from collections import deque
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        mil = 1000000
        # left (-1, -1) top right (mil, mil)
#         for i in range(1, 201):
#             blocked.append([-1, i - 1])
#             blocked.append([i - 1, -1])

#             blocked.append([-1 + i, mil])
#             blocked.append([-1, mil - i])

#             blocked.append([mil - i, -1])
#             blocked.append([mil, -1 + i])

#             blocked.append([mil, mil - i])
#             blocked.append([mil - i, mil])

        # for b in blocked:
        blocked = set(map(tuple, blocked))
        # blocked = st
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def valid(pt):
            nonlocal mil
            x, y = pt
            return 0 <= x < mil and 0 <= y < mil

        def iid(pt):
            return tuple(pt)

        def isopen(pt, tar):
            visited = set()
            nonlocal blocked, dirs
            visited.add(iid(pt))
            pt, tar = tuple(pt), tuple(tar)
            visited.add(pt)
            q = [(pt, 0)]
            dep = 0

            for cur, d in q:
                # cur = q.popleft()
                for d in dirs:
                    nd = (d[0] + cur[0], d[1] + cur[1])
                    nh = nd
                    if not valid(nd) or nh in blocked or nh in visited:
                        continue
                    if nh == tar:
                        return True
                    visited.add(nh)
                    q.append((nd, d + 1))

                if d + 1 >= 200 and len(q) > 0:
                    return True
                    # if len(q) > 20000:
                    #     return True

            return False # not enclosed

        th, sh = iid(target), iid(source)
        # if not isopen(source) and th not in visited:
        #     return False
        # # is open or is not open
        # if th in visited: # in the same patch
        #     return True

        return isopen(source, target) and isopen(target, source)
