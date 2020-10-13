import argparse

parser = argparse.ArgumentParser(description="Convert Hex to Base64")
parser.add_argument("inputHex", nargs=1)
args = parser.parse_args()

print type(args.inputHex[0])
print args.inputHex[0]
hexNum = int(args.inputHex[0], 16)

print int(hexNum, 64)
