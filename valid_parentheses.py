class Solution:
    def isValid(self, s: str) -> bool:
        parntheseses = ['(', ')', '[', ']', '{', '}']
        brackets = []
        for c in s:
            if c in '({[':
                brackets.append(c)
            else:
                if not brackets:
                    return False  # There's no matching open bracket.
                
                open_bracket = brackets.pop()
                
                if (c == ')' and open_bracket != '(') or (c == '}' and open_bracket != '{') or (c == ']' and open_bracket != '['):
                    return False  # Mismatched closing bracket.
        
        return not brackets  # All open brackets should be closed.


if __name__ == "__main__":
    print(Solution().isValid("([])"))