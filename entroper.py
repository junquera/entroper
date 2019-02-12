from entro import entropy
import sys

with open(sys.argv[1], 'rb') as f:
    a = f.read()

BLOCK_SIZE=1024
BLOCK_SIZE=256
n = len(a)/BLOCK_SIZE

n = int(n if int(n) == n else n+1)

for i in range(n):
    bloque = a[i*1024:(i*1024) + 1024]
    print(entropy(bloque))
