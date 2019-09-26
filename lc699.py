class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        sl = [(0, 0, False), (float('inf'), 0, True)]
        ans, max_h = [], 0
        for pos in positions:
            lm, rm, l = pos[0], pos[0] + pos[1], len(sl)  # most
            lb, rb = 0, len(sl) - 1
            for k, v in enumerate(sl):
                if k + 1 < l and sl[k + 1][0] >= lm:
                    lb = k
                    break

            while lb < l and sl[lb + 1][0] == lm:
                lb += 1
            h = 0
            while sl[lb][0] <= rm:
                if sl[lb][0] <= lm and sl[lb][2]:  # remove left ending
                    if sl[lb][0] == lm:
                        del sl[lb]
                    else:
                        lb += 1
                    continue
                if sl[lb][0] == rm and not sl[lb][2]:
                    break
                h = max(h, sl[lb][1])
                if sl[lb][0] < lm:
                    lb += 1
                    continue
                del sl[lb]

            h += pos[1]
            # state from here

            l, r = sl[lb - 1][1], sl[lb][1]
            sl.insert(lb, (rm, r, False))
            sl.insert(lb, (rm, h, True))
            sl.insert(lb, (lm, h, False))
            sl.insert(lb, (lm, l, True))
            max_h = max(max_h, h)
            ans.append(max_h)

            # print(sl)
        return ans
