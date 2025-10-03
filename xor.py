#!/usr/bin/env python
import argparse
import base64
import sys

def xorcrypt(data, key):
    """
    Performs XOR encryption/decryption on byte data.
    """
    return bytes(a ^ b for a, b in zip(data, key * (len(data) // len(key)) + key[:len(data) % len(key)]))

def main():
    """
    Main function to parse arguments and run the XOR cipher.
    """
    parser = argparse.ArgumentParser(
        prog='Xorpy v1.2',
        description='Stupid simple XOR encryption/decryption utility.',
        formatter_class=argparse.RawTextHelpFormatter,
        epilog='Duct taped together by Shawn Evans - sevans@nopsec.com'
    )

    # Mutually exclusive group for key input
    key_group = parser.add_mutually_exclusive_group(required=True)
    key_group.add_argument(
        '-k', '--key',
        help='Clear-text key string.'
    )
    key_group.add_argument(
        '--bk',
        help='Base64-encoded binary key string.'
    )

    # Optional arguments
    parser.add_argument(
        '-o', '--output',
        help='Output file path for the raw XORd data. If not provided, output will be base64-encoded and printed to stdout.'
    )

    parser.add_argument(
        'input_file',
        nargs='?',
        type=argparse.FileType('rb'),
        default=sys.stdin.buffer,
        help='Input file to read from. If not specified, reads from stdin.'
    )

    args = parser.parse_args()

    # Read input data
    input_data = args.input_file.read()

    # Determine the key
    if args.key:
        key_data = args.key.encode('utf-8')
    else:  # args.bk
        try:
            key_data = base64.b64decode(args.bk)
        except base64.binascii.Error:
            print("Error: The base64 key is not valid.", file=sys.stderr)
            sys.exit(1)

    # Perform the XOR operation
    result = xorcrypt(input_data, key_data)

    # Handle output
    if args.output:
        try:
            with open(args.output, 'wb') as f:
                f.write(result)
            print(f"XOR result written to '{args.output}'")
        except IOError as e:
            print(f"Error writing to file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Base64 encode the result for printing to stdout
        encoded_result = base64.b64encode(result).decode('utf-8')
        print(encoded_result)

if __name__ == "__main__":
    main()
