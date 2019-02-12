from entro import entropy
import sys

import matplotlib.pyplot as plt
import numpy as np

def main(file_path):
    file_name = file_path.split('/')[-1]

    with open(file_path, 'rb') as f:
        a = f.read()

    BLOCK_SIZE=1024

    n_blocks = 0

    n = len(a)/BLOCK_SIZE
    n_blocks = int(n if int(n) == n else n+1)

    while n_blocks < 10 and BLOCK_SIZE > 512:
        BLOCK_SIZE = int(BLOCK_SIZE * 0.9)
        n = len(a)/BLOCK_SIZE
        n_blocks = int(n if int(n) == n else n+1)

    while n_blocks > 1000 and BLOCK_SIZE < 8192:
        BLOCK_SIZE = int(BLOCK_SIZE/0.9)
        n = len(a)/BLOCK_SIZE
        n_blocks = int(n if int(n) == n else n+1)

    global_entropy = entropy(a)
    blocks = []
    entropies = []
    for i in range(n_blocks):
        bloque = a[i*BLOCK_SIZE:(i*BLOCK_SIZE) + BLOCK_SIZE]
        e = entropy(bloque)
        blocks.append(i*BLOCK_SIZE)
        entropies.append(e)

    fig, ax = plt.subplots()
    fig.suptitle('Entropy', fontsize=16)

    index = np.arange(n_blocks)

    print(n_blocks, BLOCK_SIZE, global_entropy)

    ax.bar((index * BLOCK_SIZE) + (BLOCK_SIZE/2) , entropies, BLOCK_SIZE, label="Entropy of %dB blocks" % BLOCK_SIZE)
    ax.plot((index * BLOCK_SIZE) + (BLOCK_SIZE/2) , np.repeat(global_entropy, n_blocks), '--', color='red', label="Global entropy")

    ax.set_title("%s" % (file_name))
    ax.legend(loc="lower right")

    # Entropía entre 0 y 8 (bits)
    ax.set_ylim([0,8])

    plt.show()
    
if __name__ == '__main__':
    file_path = sys.argv[1]
    main(file_path)