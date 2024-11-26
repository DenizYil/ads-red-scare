import os

from none_problem.none_problem import solve as none_solve
from few.few import solve as few_solve
from alternate.alternate import solve as alternate_solve
from some.some import solve as some_solve
from many.many import solve as many_solve
from tabulate import tabulate

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
        for i in range(0, n):
            vertices.append(lines[i + 2].strip())
        for j in range(0, m):
            edges.append(lines[j + n + 2].strip())

        # Instance name
        result.append(file)
        result.append(n)
        # Alternate
        result.append(alternate_solve(n, m, r, start, terminal, vertices, edges))
        # Few
        result.append(few_solve(n, m, r, start, terminal, vertices, edges))
        # Many
        result.append(many_solve(n, m, r, start, terminal, vertices, edges))
        # None
        result.append(none_solve(n, m, r, start, terminal, vertices, edges))
        # Some
        result.append(some_solve(n, m, r, start, terminal, vertices, edges))

    results.append(result)
out = open('results.txt', 'w', encoding='utf-8')
out.write(tabulate(results, headers=['Instance name', 'n', 'A', 'F', 'M', 'N', 'S'], tablefmt='fancy_grid'))
out.close()
