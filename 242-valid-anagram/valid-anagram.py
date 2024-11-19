# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s)!=len(t):
#             return False
#         return sorted(s)==sorted(t)
class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         d1={}
#         for i in s:
#             if i in d1.keys():
#                 d1.update({i:d1.get(i)+1})
#             else:
#                 d1[i]=1

#         d2={}
#         for i in t:
#             if i in d2.keys():
#                 d2.update({i:d2.get(i)+1})
#             else:
#                 d2[i]=1
#         if d1==d2:
#             return True
#         else:
#             return False
        def isAnagram(self, s, t):
            if len(s) != len(t):
                return False
        
            freq = [0] * 26
            for i in range(len(s)):
                freq[ord(s[i]) - ord('a')] += 1
                freq[ord(t[i]) - ord('a')] -= 1

            for i in range(len(freq)):
                if freq[i] != 0:
                    return False

            return True
