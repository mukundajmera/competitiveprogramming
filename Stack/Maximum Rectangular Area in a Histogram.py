# User function Template for python3
'''
Function Arguments :
		@param  : histogram( given list containing info about histogram)
		@return : integer
'''


class Solution:
    def getMaxArea(self, histogram):
        # code here

        stack = list()

        max_area = 0

        # iterate over histogram
        index = 0
        while (index < len(histogram)):
            # base for start and initial
            if (not stack) or (histogram[stack[-1]] <= histogram[index]):
                stack.append(index)
                index += 1

            else:

                # print(stack, "stack on pop at ", index, stack[-1])
                top_of_stack = stack.pop()
                # find area
                # value * ((right -left) + 1)
                if stack:
                    area = (histogram[top_of_stack] * (index - stack[-1] - 1))

                else:
                    # if only one bar and stack is empty
                    area = (histogram[top_of_stack] * (index))

                max_area = max(max_area, area)

        # if any remaining bars are left follow same process
        while stack:
            top_of_stack = stack.pop()

            if stack:
                area = (histogram[top_of_stack] * (index - stack[-1] - 1))
                # print(stack)
                # print('area = ', histogram[top_of_stack], '*', index - stack[-1] - 1, 'index ', index, ' stack[-1]', stack[-1])
            else:
                # if only one bar and stack is empty
                area = (histogram[top_of_stack] * (index))

            max_area = max(max_area, area)

        return max_area


# {
#  Driver Code Starts
# Initial Template for Python 3

# by Jinay Shah

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.getMaxArea(a))
# } Driver Code Ends