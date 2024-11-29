class Solution:
    def reverseString(self, s: List[str]) -> None:
        # #O(n)
        # l=0
        # r=len(s)-1
        # while(l<=r):
        #     s[l],s[r]=s[r],s[l]
        #     l+=1
        #     r-=1
            
        #O(n) stack
        stack=[]
        for c in s:
            stack.append(c)
        i=0
        while stack:
            s[i]=stack.pop()
            i+=1
        