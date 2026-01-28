# entroper

A tiny CLI that computes Shannon entropy (bits/byte) for files and data streams.

Quick summary
-------------
Measure how random a file is to detect compression, encryption, or low-entropy data.

Usage
-----
entroper [options] <path>

Examples
--------
- Measure a file:
1.   entroper file.bin

Interpretation
--------------
0 = no variability — 8 = max randomness per byte. Values >= ~7.5 usually indicate compressed/encrypted data.

Contributing
------------
Open issues, fork, make a branch, add tests/docs, and send a PR.

License
-------
See LICENSE in the repository.
