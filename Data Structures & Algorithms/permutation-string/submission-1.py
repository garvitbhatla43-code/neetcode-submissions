class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        # Fill counts for s1 and the first window of s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        if s1_count == s2_count:
            return True

        # Slide the fixed window across s2
        for r in range(len(s1), len(s2)):
            # Add new character on the right
            s2_count[ord(s2[r]) - ord('a')] += 1
            # Remove old character on the left
            l = r - len(s1)
            s2_count[ord(s2[l]) - ord('a')] -= 1

            if s1_count == s2_count:
                return True

        return False
        