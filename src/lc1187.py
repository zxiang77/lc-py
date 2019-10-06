from typing import List


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        minctr = float('inf')

        prevSorted = True
        arr1.insert(0, float('-inf'))
        s1, s2 = 0, 0
        for i in range(1, len(arr1)): # find samllest larger than prev
            if not prevSorted:
                break
            if i > 0 and arr1[i - 1] >= arr1[i]:
                prevSorted = False
            ctr = 0

            tmp = s2
            for s in range(i, len(arr1)):
                if arr1[s - 1] >= arr1[s]:
                    if tmp == len(arr2) or arr2[tmp] >= arr1[s - 1]:
                        break # no solution found here
                    ctr += 1
                while tmp < len(arr2) and arr2[tmp] <= arr1[s]:
                    tmp += 1

            if s == len(arr1):
                minctr = min(minctr, ctr)

            while s2 < len(arr2) and arr2[s2] <= arr1[i]:
                s2 += 1

        return -1 if float('inf') == minctr else minctr