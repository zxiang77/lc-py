from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.res = set()
        self.res.add("")
        self.maxlen = 0
        self.s = s
        l_total, r_total = 0, 0
        for c in s:
            if c != '(' and c != ')':
                continue
            l_total += 1 if c == '(' else 0
            r_total += 1 if c == ')' else 0

        self.dfs(0, "", 0, l_total, r_total)

        return list(self.res)

    def dfs(self, i, st, total, l_rem, r_rem): #
        if i == len(self.s):
            if total == 0:
                if len(st) > self.maxlen:
                    self.maxlen = len(st)
                    self.res = set()
                    self.res.add(st)
                elif len(st) == self.maxlen:
                    self.res.add(st)
            return
        if self.s[i] != '(' and self.s[i] != ')':
            # can be optimized by cutting off branches
            self.dfs(i + 1, st + self.s[i], total, l_rem, r_rem)
            return
        l_rem -= 1 if self.s[i] == '(' else 0
        r_rem -= 1 if self.s[i] == ')' else 0
        # sum > 0, surplus left, discard left,
        # sum < 0, surplus right, discard right
        sum = total + l_rem
        # rm
        if ((total + l_rem) > r_rem and self.s[i] == '(') \
                or ((total + l_rem) < r_rem and self.s[i] == ')') \
                or ((total + l_rem) == r_rem):
            self.dfs(i + 1, st, total, l_rem, r_rem) # not include current paren

        total += (1 if self.s[i] == '(' else -1)  # try to include
        if total >= 0:
            if ((total + l_rem) > r_rem and self.s[i] == ')') \
                    or ((total + l_rem) < r_rem and self.s[i] == '(') \
                    or ((total + l_rem) == r_rem):
                self.dfs(i + 1, st + self.s[i], total, l_rem, r_rem)


ff = None
print(str(ff))
fff = "a,3,4,2"
print(fff.split(","))

gg = []
f22 = ",".join(gg)
print(f22)
print(f22.split(","))

st = []
st