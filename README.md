# Xorpy

Xorpy is handy XOR encryption tool. This tool takes input from a text file or stdin, and will XOR encrypt it using a user defined key. Due to the nature of bit flipping, the same function that encrypts will also decrypt, assuming you provide the correct key. Use this as a standalone app, or copy/paste it into your own project. It's simple, but works well enough.

```
usage: Xorpy v1.2 [-h] (-k KEY | --bk BK) [-o OUTPUT] [input_file]

Stupid simple XOR encryption/decryption utility.

positional arguments:
  input_file            Input file to read from. If not specified, reads from stdin.

options:
  -h, --help            show this help message and exit
  -k KEY, --key KEY     Clear-text key string.
  --bk BK               Base64-encoded binary key string.
  -o OUTPUT, --output OUTPUT
                        Output file path for the raw XORd data. If not provided, output will be base64-encoded and printed to stdout.

Duct taped together by Shawn Evans - sevans@nopsec.com

```
