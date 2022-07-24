
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        b = 0
        while x > b:
            b = b * 10 + x % 10
            x /= 10

        return x == b or x == b / 10

'''
        Solution 

        1234

        1221
        12
        12

        12321
        12
        12

        12
        43

        1. reverse half of the number, compare it with our original number

        even    x  b
        1221 -> 12 12 -> true
        1231 -> 12 13 -> false
        1321 -> 1  123 -> false

        odd      x.  b   b/10
        12321 -> 12  123  12    -> true
        12322 -> 12  223  22    -> false

        1230
        1210 -> 121
        b -> 12
        x -> 1

        Time O(n)
        Space O(1)
        n is the number of digits


'''