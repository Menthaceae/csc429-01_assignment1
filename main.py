import node
import bfs
import dfs
import dls

A = node.Node("A")
B = node.Node("B")
C = node.Node("C")
D = node.Node("D")
E = node.Node("E")
F = node.Node("F")
A.add([B])
B.add([C, D])
C.add([E])
D.add([F])

print("\n___________________________________\n")
# Part A
print("Part A")
bfs.bfs(A, E)
print("\n___________________________________\n")

# Part B
print("Part B")
dfs.dfs(A, E)
print("\n___________________________________\n")

# Part C
"""
H 
G I J K L M
F     N 
E     B 
D   P O 
C   Q 
A S R 
"""
A = node.Node("A")
B = node.Node("B")
C = node.Node("C")
D = node.Node("D")
E = node.Node("E")
F = node.Node("F")
G = node.Node("G")
H = node.Node("H")
I = node.Node("I")
J = node.Node("J")
K = node.Node("K")
L = node.Node("L")
M = node.Node("M")
N = node.Node("N")
O = node.Node("O")
P = node.Node("P")
Q = node.Node("Q")
R = node.Node("R")
S = node.Node("S")
A.add([C, S])
B.add([N, O])
C.add([A, D])
D.add([E, C])
E.add([F, D])
F.add([E, G])
G.add([H, F, I])
H.add([G])
I.add([G, J])
J.add([I, K])
K.add([J, L, N])
L.add([K, M])
M.add([L])
N.add([K, B])
O.add([B, P])
P.add([O, Q])
Q.add([P, R])
R.add([Q, S])
S.add([A, R])


print("Part C")
bfs.bfs(A, B)
print("\n___________________________________\n")

print("Part D")
dfs.dfs(A, B)
print("\n___________________________________\n")

print("DLS")
dls.dls(A, B, 2)