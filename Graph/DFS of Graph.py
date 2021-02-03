class Solution:
    def findDFS(self, s, adj, visited):
        self.res.append(s)
        self.visited[s] = True
        for u in adj[s]:
            if self.visited[u] == False:
                self.findDFS(u, adj, self.visited)

    def dfsOfGraph(self, V, adj):
        # code here
        self.visited = [False] * V
        self.res = []
        for i in range(V):
            if self.visited[i] == False:
                self.findDFS(i, adj, self.visited)
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
            adj[v].append(u)
        ob = Solution()
        ans = ob.dfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()

# } Driver Code Ends