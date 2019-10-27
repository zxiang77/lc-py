from typing import List

# TODO: document this one before forgetting
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        def helper(s4r, start, prevdel, params):
            l = len(s4r)
            cnt = 0
            for i in range(start, l):
                # assumption here: s4r[0: i] is valid prefix
                cnt += 1 if s4r[i] == params[0] else 0
                cnt -= 1 if s4r[i] == params[1] else 0
                if cnt >= 0:
                    continue

                # assumption failed, so we need to remove 1 ending param from last deletion point
                for j in range(prevdel, i + 1):
                    if s4r[j] == params[1] and (j == prevdel or s4r[j - 1] != params[1]):
                        helper(s4r[0: j] + s4r[j + 1], i, j, params)
                return
            reverse = s4r[::-1]
            if params[0] == '(':
                # the param reverse here is hard to imagine, but thinking it in a way to interchange params and reuse param
                # would be easier to imagine, though two works in the similar way
                helper(reverse, 0, 0, params[::-1])
            else:
                res.append(reverse)

        helper(s, 0, 0, ['(', ')'])
        return res

class Solution2:
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
