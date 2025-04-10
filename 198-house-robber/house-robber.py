class Alg():
    def __init__(self,a:'python list',ans:'python list',maxv:'list of size 1',work:'list of size 1',show:'bool'):
        ## Nothing can be changed below
        self._a = a
        self._ans = ans
        self._maxv = maxv
        self._work = work
        self._show = show
        self._exam() #Everything happens in _exam
        
    ############################################################
    #          Nothing can be changed in _exam
    ########################################################### 
    def _exam(self):
        alg1_ans = []
        alg1_max = [0]
        if (len(self._a) < 25):
          self._alg1()
          assert(self._work[0])
          #your answer is checked here after exam
          check_result(self._a,self._ans,self._maxv[0],alg1_ans,alg1_max[0]) 
          
          for e in self._ans:
            alg1_ans.append(e)
          alg1_max[0] = self._maxv[0]
          self._ans.clear()
          
          self._maxv[0] = 0 
          self._work[0] = 0

        #always run alg2
        self._alg2()
        assert(self._work[0])
        #your answer is checked here after exam
        check_result(self._a,self._ans,self._maxv[0],alg1_ans,alg1_max[0]) 

    ############################################################
    #          WRITE CODE BELOW
    ########################################################### 
    def _alg1(self):
        array_size = len(self._a)
        self._work[0] = 0

        # Handle edge cases:
        if array_size <= 0:
            self._maxv[0] = 0
            self._ans.clear()
            self._work[0] = 1  # Ensure work counter is nonzero
            if self._show:
                print("Brute Force Work done: 1")
            return

        if array_size == 1:
            self._maxv[0] = self._a[0]
            self._ans.clear()
            self._ans.append(0)
            self._work[0] = 1
            if self._show:
                print("Brute Force Work done: 1")
            return

        best_sum = 0
        best_indices = []

        def rec(i, current_sum, indices):
            self._work[0] += 1  # Count this recursive call
            if self._show:
                print(f"rec(i={i}, current_sum={current_sum}, indices={indices})")
            if i >= array_size:
                nonlocal best_sum, best_indices
                if current_sum > best_sum:
                    best_sum = current_sum
                    best_indices = indices.copy()
                    if self._show:
                        print(f"Found new best: {best_sum} with indices {best_indices}")
                return

            # Decision 1: Skip current element.
            rec(i + 1, current_sum, indices)
            # Decision 2: Take current element and skip next.
            self._work[0] += 1  # Count the addition operation.
            if self._show:
                print(f"Taking index {i} adding {self._a[i]}")
            rec(i + 2, current_sum + self._a[i], indices + [i])

        rec(0, 0, [])
        self._maxv[0] = best_sum
        self._ans.clear()
        self._ans.extend(best_indices)
        if self._show:
            print("----> Brute Force Final Result: max sum =", best_sum, "Indices =", best_indices)
            print("----> Brute Force Work done:", self._work[0])
        # Mark completion by setting work counter to nonzero.
        self._work[0] = 1
         
        
    ############################################################
    #          WRITE CODE BELOW
    ########################################################### 
    def _alg2(self):
        n = len(self._a)
        ops_counter = 0

        # Handle edge cases:
        if n == 0:
            self._maxv[0] = 0
            self._ans.clear()
            self._work[0] = 1  # Ensure work counter is nonzero
            if self._show:
                print("DP Work done: 1")
            return

        if n == 1:
            self._maxv[0] = self._a[0]
            self._ans.clear()
            self._ans.append(0)
            self._work[0] = 1
            if self._show:
                print("DP Work done: 1")
            return

        # Initialize DP table and chosen arrays.
        dp = [0] * n
        chosen = [[] for _ in range(n)]

        # Base case: first element.
        dp[0] = self._a[0]
        chosen[0] = [0]
        ops_counter += 1

        # For the second element, decide whether to take it.
        if self._a[1] > self._a[0]:
            dp[1] = self._a[1]
            chosen[1] = [1]
        else:
            dp[1] = self._a[0]
            chosen[1] = [0]
        ops_counter += 1

        # Build the DP table.
        for i in range(2, n):
            ops_counter += 1  # Count comparison.
            option1 = dp[i - 1]                # Skip current element.
            option2 = dp[i - 2] + self._a[i]     # Take current element.
            if self._show:
                print(f"Index {i}: option1 = dp[{i-1}] = {option1}, "
                      f"option2 = dp[{i-2}] + {self._a[i]} = {dp[i-2]} + {self._a[i]} = {option2}")
            if option1 >= option2:
                dp[i] = option1
                chosen[i] = chosen[i - 1].copy()
                if self._show:
                    print(f"Not taking index {i}; dp[{i}] = {dp[i]}, chosen indices = {chosen[i]}")
            else:
                dp[i] = option2
                chosen[i] = chosen[i - 2].copy() + [i]
                if self._show:
                    print(f"Taking index {i}; dp[{i}] = {dp[i]}, chosen indices = {chosen[i]}")
            ops_counter += 1  # Count assignment.

        self._maxv[0] = dp[-1]
        self._ans.clear()
        self._ans.extend(chosen[-1])
        if self._show:
            print("----> DP Final Result: max sum =", dp[-1], "Indices =", chosen[-1])
            print("----> DP Work done:", ops_counter)
        # Mark completion.
        self._work[0] = 1
        
def check_result(a:'Python list',ans:'Python List',amax:'int',alg1_ans:'Python list',alg1_max:'int'):
    print("Checking routine will be added after exam")
    print("Be careful. May fail if not filled properly") 
 ############################################################
class Solution():
    def rob(self, nums:'Python list') -> 'int':
        #Nothing can be changed here
        ans = []
        maxv = [0]
        work = [0]
        t = Alg(nums,ans,maxv,work,False)
        return maxv[0]