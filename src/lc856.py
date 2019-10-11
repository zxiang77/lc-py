class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stk = []
        for i in S:
            if i == '(':
                stk.append(None)
            else:
                if stk[-1] == None:
                    stk.pop()
                    stk.append(1)
                else:
                    su = 0
                    while stk[-1] != None:
                        su += stk[-1]
                        stk.pop()
                    stk.pop()
                    stk.append(su * 2)

        return sum(stk)
