from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            sym = strs[0][i]
            for s in strs:
                try:
                    if s[i] != sym:
                        return strs[0][:i]
                except IndexError:
                    return strs[0][:i]
        return strs[0] # this executes when strs is empty or strs has only one element or strs has only one character or strs has only one character and it is the same for all elements


if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))
