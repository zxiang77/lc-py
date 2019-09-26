class Solution:
    def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
        # cmp for numbers
        # 1. can have all combs with less digits
        # for same digits
        # 2. (# of less first digit) x all the combs with (n - 1) digits
        # 3. (# of same first digits): 1 x recurse step 2 with num[1:]

        # reusable parts
        Nar = list(str(N))
        ctr = [0] * (len(Nar))

        for i in range(len(Nar) - 1, 0, -1):
            if i == len(Nar) - 1 and i > 0:
                ctr[i] = len(D)
                continue
            ctr[i] = ctr[i + 1] * len(D)

        for i in range(len(Nar)):
            n = int(Nar[i])
            # if n == 0:
            # continue
            for j in range(len(D)):
                d = int(D[j])
                if d < n:
                    ctr[0] += ctr[i + 1] if (i + 1) < len(Nar) else 1
                elif d == n:
                    if i == len(Nar) - 1:
                        ctr[0] += 1
                    break
                else:
                    return sum(ctr)
                if len(D) - 1 == j and d < n:
                    return sum(ctr)
        return sum(ctr)

max()