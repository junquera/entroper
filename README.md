# entroper

A tiny CLI that computes Shannon entropy (bits/byte) for files and data streams.

Quick summary
-------------
Measure how random a file is to detect compression, encryption, or low-entropy data.

Usage
-----
entroper [options] <path|->  
Use `-` or omit the path to read from stdin.

Examples
--------
- Measure a file:
  entroper file.bin

- From a pipe:
  gzip -c image.png | entroper -

- JSON output:
  entroper --json file.bin

Common options
--------------
- -h, --help        Show help
- -j, --json        Output JSON
- -H, --hist        Print byte-value histogram (0x00–0xFF)
- -b, --block-size N  Process in blocks of N bytes
- --per-block       Show entropy per block
- --threshold T     Exit nonzero if entropy above/below T

Interpretation
--------------
0 = no variability — 8 = max randomness per byte. Values >= ~7.5 usually indicate compressed/encrypted data.

Contributing
------------
Open issues, fork, make a branch, add tests/docs, and send a PR.

License
-------
See LICENSE in the repository.
