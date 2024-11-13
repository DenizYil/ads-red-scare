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
        print(f)
        n, m, r = [int(i) for i in f.readline().split()]
        start, terminal = [str(i) for i in f.readline().split()]

        vertices = []
        edges = []
        for i in range(2, 2+n):
            vertices.append(str(f.readline()))
        # for j in range(n+4, len(lines)):
        #    edges.append(lines[j])

        result.append(none_solve(n, m, r, start, terminal, vertices, edges))
        # result.append(few_solve(n, m, r, start, terminal, vertices, edges))

    results.append(result)
    break
