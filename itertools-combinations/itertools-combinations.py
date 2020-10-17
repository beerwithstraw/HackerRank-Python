# Code in Python3
from itertools import combinations
string, length = input().split()
for i in range (1,int(length)+1):
    output = ["".join(sorted(i)) for i in combinations(string,i)]
    output.sort()
    print("\n".join(output))
