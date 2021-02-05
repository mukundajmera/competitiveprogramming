for adjs in adj[source]:
    # call in recurssion for all unvisited nodes
    if self.visited[adjs] == False:
        # same check in iteration for all adjs Edge cases
        if self.cyclic(adjs, adj, source):
            return True
    # elseif for visited nodes check if not parent
    # hence visited node adjs means cyclic
    elif parent != adjs:
        return True


def isCycle(self, V, adj):
    # Code here
    self.visited = [False] * V
    self.res = False
    for vertex in range(V):
        if self.visited[vertex] == False:
            if self.cyclic(vertex, adj, -1) == True:
                return True
    return False


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
        obj = Solution()
        ans = obj.isCycle(V, adj)
        if (ans):
            print("1")
        else:
            print("0")

# } Driver Code Ends