import sys
import math

album, avg = map(int, sys.stdin.readline().split())

melody = 2*(math.sqrt(album * avg))

print(melody)