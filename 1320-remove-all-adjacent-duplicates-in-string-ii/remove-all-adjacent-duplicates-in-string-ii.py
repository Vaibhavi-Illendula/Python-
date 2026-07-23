class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st=[]
        for ch in s:
            if st and st[-1][0]==ch:
                st[-1][1]+=1
                if st[-1][1]==k:
                    st.pop()
            else:
                st.append([ch,1])
        res=""
        for ch,cnt in st:
            res+=cnt*ch
        return res

        