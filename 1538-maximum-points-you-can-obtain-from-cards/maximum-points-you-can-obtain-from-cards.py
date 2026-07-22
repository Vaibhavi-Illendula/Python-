class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left=k-1
        right=len(cardPoints)-1
        c_s=sum(cardPoints[:k])
        m_s=c_s
        while left>=0:
            c_s-=cardPoints[left]
            c_s+=cardPoints[right]
            m_s=max(m_s,c_s)
            left-=1
            right-=1
        return m_s

        