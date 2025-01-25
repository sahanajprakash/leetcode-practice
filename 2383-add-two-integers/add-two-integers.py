class Int:
    def __init__(self, value=0):
        self._value = value

    def int(self):
        return self._value

    def __eq__(self, other):
        return self._value == other._value

    def __ne__(self, other):
        return self._value != other._value

    def __lt__(self, other):
        return self._value < other._value

    def __le__(self, other):
        return self._value <= other._value

    def __gt__(self, other):
        return self._value > other._value

    def __ge__(self, other):
        return self._value >= other._value

    def __add__(self, other):
        return Int(self._value + other._value)

    def __str__(self):
        return str(self._value)
###########################################################
# WRIRE  class  Int
###########################################################


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
class Exam:
    def __init__(self, a: 'Int', b: 'Int', add: 'Int', relation: 'list of bool') -> 'None':
        # Compute addition and update add directly
        add._value = (a + b).int()

        # Compute relations based on Boolean logic
        less_than = a < b
        greater_than = a > b
        equal_to = not less_than and not greater_than

        # Populate the relation list
        relation.extend([
            less_than,            # a < b
            less_than or equal_to, # a <= b
            greater_than,         # a > b
            greater_than or equal_to, # a >= b
            equal_to,             # a == b
            not equal_to          # a != b
        ])
