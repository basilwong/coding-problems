class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer

    def same_length(self, digits, sorted_digits, index, target):
        if index == len(target):
            return 0
        count = 0
        for digit in sorted_digits:
            if index == 0 and digit == 0 and len(target) > 1:
                continue
            if digit == target[index]:
                count += self.same_length(digits, sorted_digits, index + 1, target)
            elif digit < target[index]:
                count += len(digits)**(len(target) - index - 1)
            else:
                break
        return count

    # @return an integer
    def solve(self, A, B, C):

        target = [int(x) for x in str(C)]
        digits = set(A)
        sorted_digits = sorted(A)

        # Solution if B is not the exact size of the target.
        if B > len(target):
            return 0
        elif B < len(target):
            if 0 in digits and B > 1:
                return (len(A) - 1)*(len(A)**(B-1))
            else:
                return len(A)**B

        return self.same_length(digits, sorted_digits, 0, target)


if __name__ == "__main__":
    s = Solution()
    print(s.solve([0, 1, 2, 5], 1, 123))
