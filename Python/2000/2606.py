graph={}
computer = int(input())
for i in range(1, computer+1):
  graph[i] = []
for i in range(int(input())):
  n1, n2 = map(int, input().split())
  if n2 not in graph[n1]:
    graph[n1].append(n2)
  if n1 not in graph[n2]:
    graph[n2].append(n1)

def virus(graph):
    visited = []
    stack = [1]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                stack += temp
    return len(visited)
print(virus(graph)-1)
