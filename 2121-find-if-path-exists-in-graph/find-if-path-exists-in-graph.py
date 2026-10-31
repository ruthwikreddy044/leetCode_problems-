class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = [[] for i in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False]*n
        q = []
        q.append(source)
        visited[source] = True
        while len(q)>0:
            a = q.pop(0)
            if a == destination:
                return True
            for i in graph[a]:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True
        return False