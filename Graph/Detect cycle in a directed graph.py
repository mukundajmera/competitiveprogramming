# User function Template for python3
import sys

sys.setrecursionlimit(100000)


class Solution:
    def isCyclic(self, V, adj):
        # code here
        visited = [False] * V
        restack = [False] * V
        for source in range(V):
            if self.dfs(source, adj, visited, restack) == True:
                return True
            else:
                return False

    def dfs(self, source, adj, visited, restack):
        visited[source] = True
        restack[source] = True
        for node in adj[source]:
            if visited[node] == False:
                if self.dfs(node, adj, visited, restack):
                    return True
            elif restack[node] == True:
                return True
        restack[node] = False
        return False


# {
#  Driver Code Starts
# Initial Template for Python 3

import sys

sys.setrecursionlimit(10 ** 6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends