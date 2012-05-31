from bitarray import bitarray

def bitmap_sort(nums, n):
    arr = (n + 1) * bitarray('0')
    for num in nums:
        arr[num] = 1

    return (i for (i, bit) in enumerate(arr) if bit)

if __name__ == '__main__':
    import sys
    n = int(sys.argv[1])
    nums = (int(line) for line in sys.stdin)

    for i in bitmap_sort(nums, n):
        print i
