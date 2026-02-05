import node
import bfs
import dfs

F = node.Node("F", [])
E = node.Node("E", [])
D = node.Node("D", [F])
C = node.Node("C", [E])
B = node.Node("B", [C, D])
A = node.Node("A", [B])

dfs.dfs(B, E)
print("\n")
bfs.bfs(A, E)