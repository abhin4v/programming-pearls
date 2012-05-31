from bitarray import bitarray

if __name__ == '__main__':
    import sys
    n = int(sys.argv[1])
    arr = (n + 1) * bitarray('0')

    for line in sys.stdin:
        num = int(line)
        arr[num] = 1

    for (i, bit) in enumerate(arr):
        if bit:
            print i
        
