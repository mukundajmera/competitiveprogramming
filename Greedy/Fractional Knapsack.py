# User function Template for python3

class Solution:
    def fractionalknapsack(self, W, Items, n):
        '''
        :param W: max weight which can be stored
        :param Items: List contianing Item class objects as defined in driver code, with value and weight
        :param n: size of Items
        :return: Float value of max possible value, two decimal place accuracy is expected by driver code

        {
            class Item:
            def __init__(self,val,w):
                self.value = val
                self.weight = w
        }
        '''
        # code here
        Items.sort(key=lambda item: item.value / item.weight, reverse=True)
        max_weight = W
        value = 0
        for item in Items:
            # print(item.value, item.weight)
            if max_weight >= item.weight:
                max_weight -= item.weight
                value += item.value
            else:
                # partial value
                value += max_weight * (item.value / item.weight)
                max_weight = 0
                break

        return value


# {
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys


# Contributed by : Nagendra Jha

class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, W = map(int, input().strip().split())
        info = list(map(int, input().strip().split()))
        Items = [Item(0, 0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2 * i]
            Items[i].weight = info[2 * i + 1]

        ob = Solution()
        print("%.2f" % ob.fractionalknapsack(W, Items, n))

# } Driver Code Ends