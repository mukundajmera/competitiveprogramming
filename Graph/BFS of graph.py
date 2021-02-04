from collections import deque


class Solution:
    def bfsGraph(self, adj, source, visited):
        q = deque()
        q.append(source)
        visited[source] = True
        while q:
            s = q.popleft()
            self.res.append(s)
            # print(source,end="")
            # traverse adjs
            for i in adj[s]:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True

    def bfsOfGraph(self, V, adj):
        # code here
        visited = [False] * V
        self.res = []
        for i in range(V):
            if visited[i] == False:
                self.bfsGraph(adj, i, visited)
                return self.res


# {
#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
        ob = Solution()
        ans = ob.bfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()

# } Driver Code Ends