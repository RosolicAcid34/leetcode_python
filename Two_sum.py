##brute force approachh
class solve:
    def Two_sum(self,numbers, Target):
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                sum = numbers[i]+numbers[j]
                if sum == Target:
                    return[i, j]

# as for two loops , so the complexity will be O(n^2)
#let's go for a better solution with data structure.

"""
let's use hashmap for this solution.
"""
class solution:
    def twosum(self, numbers: list[int], target: int) -> list[int]:
        input_list = {}
        for i, n in enumerate(numbers):
            comp = target - n
            if comp in input_list:
                return [input_list[comp]+1, i+1]
            input_list[n] = i

"""
so, using hash map we can reduce complexity to O(n)
and also,
Runtime: 117 ms, faster than 46.60% of Python3 online submissions for Two Sum.
Memory Usage: 15.1 MB, less than 50.46% of Python3 online submissions for Two Sum.
"""
