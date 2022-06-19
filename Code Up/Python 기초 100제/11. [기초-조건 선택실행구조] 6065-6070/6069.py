import sys
chr = sys.stdin.readline().rstrip()

dict = {
    'A' : 'best!!!',
    'B' : 'good!!',
    'C' : 'run!',
    'D' : 'slowly~',
}
try:
    print(dict[chr])
except:
    print('what?')