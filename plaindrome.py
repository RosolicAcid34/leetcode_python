
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """ """
        temp = x
        reverse = 0
        while x > 0:
            reverse *= 10
            reverse += x % 10
            x //= 10
        return temp == reverse

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