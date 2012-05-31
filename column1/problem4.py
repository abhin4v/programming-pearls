import random

def k_uniq_rand_nums_of_n(n, k):
    nums = [0]
    for i in xrange(1, n):
        nums.append(i)
        j = random.randint(0, i)
        nums[i] = nums[j]
        nums[j] = i

    return nums[:k]

if __name__ == '__main__':
    import sys
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    for i in k_uniq_rand_nums_of_n(n, k):
        print i
        
