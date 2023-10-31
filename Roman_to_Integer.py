class solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0
        else:
            map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
            result = 0
            for i in range(len(s)):
                if i < len(s) -1 and map[s[i]] < map[s[i+1]]:
                    result -= map[s[i]]
                    print(result)
                else:
                    result += map[s[i]]
            return result

if __name__ == '__main__':
    s = solution()
    print(s.romanToInt('LVIII'))               