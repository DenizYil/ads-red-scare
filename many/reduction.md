# Many reduction
Here is the reduction *Longest path* $<_p$ *Many*.
**Claim**: Many is NP-hard
**Proof**: We will reduce from longest path which is known to be NP-hard
Let G, k be an instance of longest path.
G has with vertex set V(G) and edge set E(G).
G has no cycles.
The desired output is *yes* if G contains a path of k or more edges, and no otherwise

Construct an instance of G', k'  of Many that consist only of red vertices. ie.
$V(G) \in R$. Finally, set k' = k.

For instance if we have the following graph:
[longest path and many graph](./longest path  - Many - reduction.png)
Then the resulting path where k=3 for *many* is going to return is the path p: `s -> A -> C -> t` 
Now assume that p is a solution to the Many instance.
In other words, the union of the k' sets in G contains all of G'.



