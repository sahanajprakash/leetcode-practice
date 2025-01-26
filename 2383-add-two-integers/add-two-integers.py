class Solution:
    def sum(self, a: int, b: int) -> int:
        c = a + b
        relation = []
        relation.append(a < b)
        relation.append(a <= b)
        relation.append(a > b)
        relation.append(a >= b)
        relation.append(a == b)
        relation.append(a != b)
        #All above must work. Now make sure Int works
        ma = Int(a)
        ma1 = Int(a)
        mb = Int(b)
        mb1 = Int(b)
        madd = Int()
        mrelation = []
        s = Exam(ma,mb,madd,mrelation)
        assert(ma == ma1)
        assert(mb == mb1)
        ans = madd.int()
        assert(c == ans)
        for i in range(len(relation)):
          assert(relation[i] == mrelation[i])
        return ans


########################################
# WRITE CODE BELOW
########################################
class Exam:
    def __init__(self, a:'Int', b:'Int', add:'Int',relation:'list of bool')->'None':
         # Use Int class logic to perform operations
        result = a + b
        add._a = result._a
        add._positive = result._positive

        # Populate relations
        relation.append(a < b)
        relation.append(a <= b)
        relation.append(a > b)
        relation.append(a >= b)
        relation.append(a == b)
        relation.append(a != b)
############################################################
# Int.py
# Implements Int object
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2025
# added to git
###########################################################

class Int:
    def __init__(self, n: int = 0):
        self._positive = n >= 0
        self._a = self.build(abs(n))

    def build(self, n: int) -> 'list of int':
        return [int(x) for x in str(n)]

    def int(self) -> int:
        value = int("".join(map(str, self._a)))
        return value if self._positive else -value

    def __len__(self):
        return len(self._a)

    def __getitem__(self, index: int) -> int:
        return self._a[index]

    def __setitem__(self, index: int, value: int):
        self._a[index] = value

    def __str__(self) -> str:
        sign = "" if self._positive else "-"
        return sign + "".join(map(str, self._a))

    def __eq__(self, other: 'Int') -> bool:
        return self.int() == other.int()

    def __lt__(self, other: 'Int') -> bool:
        return self.int() < other.int()

    def __le__(self, other: 'Int') -> bool:
        return self.int() <= other.int()

    def __gt__(self, other: 'Int') -> bool:
        return self.int() > other.int()

    def __ge__(self, other: 'Int') -> bool:
        return self.int() >= other.int()

    def __ne__(self, other: 'Int') -> bool:
        return self.int() != other.int()

    def __add__(self, other: 'Int') -> 'Int':
        if self._positive == other._positive:
            # Add absolute values
            result = self._ripple_carry_add(self._a, other._a)
            return Int(int("".join(map(str, result))) * (1 if self._positive else -1))
        else:
            # Handle subtraction of absolute values
            if self._absolute_gte(self._a, other._a):  # self >= other
                result = self._ripple_carry_sub(self._a, other._a)
                return Int(int("".join(map(str, result))) * (1 if self._positive else -1))
            else:  # self < other
                result = self._ripple_carry_sub(other._a, self._a)
                return Int(int("".join(map(str, result))) * (-1 if self._positive else 1))

    def _absolute_gte(self, a: 'list of int', b: 'list of int') -> bool:
        """
        Helper method to determine if absolute value of `a` >= absolute value of `b`.
        """
        if len(a) > len(b):
            return True
        if len(a) < len(b):
            return False
        return a >= b  # Lexicographical comparison for equal lengths


    def __sub__(self, other: 'Int') -> 'Int':
        # Subtract by adding the negative
        neg_other = Int(-other.int())
        return self + neg_other

    def _ripple_carry_add(self, a: 'list of int', b: 'list of int') -> 'list of int':
        # Ensure `a` is the longer list
        if len(a) < len(b):
            a, b = b, a

        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        # Add digits from the least significant to the most significant
        while i >= 0 or j >= 0 or carry:
            digit_a = a[i] if i >= 0 else 0
            digit_b = b[j] if j >= 0 else 0
            total = digit_a + digit_b + carry
            result.append(total % 10)
            carry = total // 10
            i -= 1
            j -= 1

        return result[::-1]  # Reverse for the correct order

    def _ripple_carry_sub(self, a: 'list of int', b: 'list of int') -> 'list of int':
        # Subtract `b` from `a` assuming `a >= b`
        result = []
        borrow = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0:
            digit_a = a[i]
            digit_b = b[j] if j >= 0 else 0
            diff = digit_a - digit_b - borrow

            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0

            result.append(diff)
            i -= 1
            j -= 1

        # Remove leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return result[::-1]  # Reverse for the correct order





###########################################################
# WRIRE  class  Int
###########################################################

