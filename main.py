import sys
import subprocess

if len(sys.argv) > 1 and (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
    print("USAGE: python3 main.py ADVENT_DAY PART")
    sys.exit(0)

if len(sys.argv) < 3:
    print("Error, not enough parameters")
    sys.exit(1)

day = sys.argv[1]
part = sys.argv[2]

subprocess.run(['./run.sh', day, part])
