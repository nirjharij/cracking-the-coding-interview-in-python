class Solution:
    def permute(self, nums):
        output = []
        out = self.get_permutations(nums, 0, len(nums) - 1, output)
        return out

    def get_permutations(self, a, l, r, out):
        if l == r:
            n = a.copy()
            out.append(n)
            return out
        else:
            for i in range(l, r + 1):
                a[l], a[i] = a[i], a[l]
                out = self.get_permutations(a, l + 1, r, out)
                a[l], a[i] = a[i], a[l]
            return out


s = Solution()
print(s.permute([1, 2, 3]))
