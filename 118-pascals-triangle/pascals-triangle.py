class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        init = [[1]]
        if numRows == 1:
            return init
        for i in range(1, numRows):
            top = init[-1]
            new =[]
            for j in range(len(top)):
                if j-1<0:
                    new.append(1)
                else:
                    new.append(top[j-1]+top[j])
            new.append(1)
            init.append(new)
        return init


            
        