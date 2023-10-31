class Solution:
    def isPalindrome_withSlice(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x = str(x)
            return x == x[::-1]

    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        while(x>0):
            dig = x%10
            print("dig: "+str(dig))
            rev = rev*10+dig
            print("rev: "+str(rev))
            x = x//10
            print("x: "+str(x))
        if(temp == rev):
            return "Palindrome"
        else:
            return "Not Palindrome"

    def isPalindrome_withString(self, x: int) -> bool:
        length = len(str(x))
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            print("length: "+str(length))
            print("length//2: "+str(length//2))
            for i in range(length//2):
                if str(x)[i] != str(x)[length-i-1]:
                    print("str(x)[i]: "+str(str(x)[i]))
                    print("str(x)[length-i-1]: "+str(str(x)[length-i-1]))
                    return False
                print("str(x)[i]: "+str(str(x)[i]))
                print("str(x)[length-i-1]: "+str(str(x)[length-i-1]))
            return True



if __name__ == '__main__':
    x = 1221
    print(Solution().isPalindrome_withSlice(x))
    print(Solution().isPalindrome(x))
    print(Solution().isPalindrome_withString(x))