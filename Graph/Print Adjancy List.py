#User function Template for python3

class Solution:
    def printGraph(self, V, adj):
        # code here
        adj_list = []
        for i in range(V):
            temp = [i]
            temp.extend(adj[i])
            adj_list.append(temp)
        return adj_list


#{
#  Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.printGraph(V, adj)
		for i in range(len(ans)):
		    for j in range(len(ans[i])-1):
		        print(ans[i][j], end = "-> ")
		    print(ans[i][len(ans[i])-1]);

# } Driver Code Ends