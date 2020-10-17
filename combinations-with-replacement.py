#Code in Python3
from itertools import combinations_with_replacement
string, length= input().split()
output = ["".join(sorted(i)) for i in combinations_with_replacement(string, int(length))]
output.sort()
print("\n".join(output))
