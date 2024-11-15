import os

from none_problem.none_problem import solve as none_solve
from few.few import solve as few_solve
# import OS module
# Get the list of all files and directories
path = "./data/"
dir_list = os.listdir(path)


files = [file for file in os.listdir(path)]
results = []
for file in files:
    result = []
    with open(path + file) as f:
        lines = f.readlines()

        n, m, r = [int(i) for i in lines[0].split()]
        start, terminal = lines[1].split()

        vertices = []
        edges = []
        for i in range(2, n):
            vertices.append(lines[i].strip())
        for j in range(n, m):
            edges.append(lines[j].strip())

        result.append(none_solve(n, m, r, start, terminal, vertices, edges))
        # result.append(few_solve(n, m, r, start, terminal, vertices, edges))

    results.append(result)

print(results)
