class Solution:
    def removeDuplicates(self, s: str) -> str:
        n = len(s)
        st = []

        for i in range(n):
            if len(st) == 0:
                st.append(s[i])
                continue
            if st[-1]==s[i]:
                st.pop()
                continue
            st.append(s[i])
        res = []
        while len(st)>0:
            res.append(st.pop())
        res.reverse()
        return "".join(res)