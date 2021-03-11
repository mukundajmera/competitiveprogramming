#code
testCases = int(input())
arr = []
while testCases > 0:
    size = int(input())
    for i in range(1):
        arr = list(map(int, input().split()))

    MAX = max(arr)
    MIN = min(arr)
    print(MAX, MIN)
    testCases -=1