import argparse
from lib import parse_str, desc

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--string', default = None)
parser.add_argument('-f', '--file', default = None)
parser.add_argument('-d', '--desc', default = None)
args = parser.parse_args()

# If no arguments are provided, print sample "Hello World!"
if all(arg == None for arg in vars(args).values()):
    print("[" + parse_str("<F>\"hE%lo <R>w@`5d") + "]!")

if args.string != None:
    print("[" + parse_str(args.string) + "]")
if args.file != None:
    with open(args.file) as fp:
        input = fp.read()
    print("[" + parse_str(input) + "]")
if args.desc != None:
    print(desc(args.desc))