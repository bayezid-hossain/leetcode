class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        s1FreqMap=[0]*26
        s2FreqMap=[0]*26
        diff=0

        for i in range(len(s1)):
            s1_ch=s1[i]
            s2_ch=s2[i]

            if s1_ch!=s2_ch:
                diff+=1
                if diff>2:
                    return False
            s1FreqMap[ord(s1_ch)-ord('a')]+=1
            s2FreqMap[ord(s2_ch)-ord('a')]+=1
        
        return s1FreqMap==s2FreqMap
            