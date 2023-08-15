from collections import Counter
class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        a=Counter(A)
        b=Counter(B)
        c=Counter(C)
        arr=[]
        for i in a:
            if i in b and i in c:
                arr.append(i)
        arr=sorted(arr)
        return arr