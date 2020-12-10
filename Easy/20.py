dict = {')': '(', '}': '{', ']': '['}
class Solution:
    # @return a boolean
    def isValid(self, strs) -> bool:
        pares = []
        for s in strs:
            if s in dict.values():
                pares.append(s)
            elif s in dict.keys():
                if pares == [] or dict[s] != pares.pop():
                    return False
            else:
                return False
        return pares == []
