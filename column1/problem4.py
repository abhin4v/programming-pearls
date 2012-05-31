import random

def k_uniq_rand_nums_of_n(n, k):
    nums = [0] * n
    for i in xrange(n - 1, n - 1 - k, -1):
        j = random.randint(0, i)

        num_j = nums[j] 
        if num_j == 0:
            num_j = j + 1

        num_i = nums[i] 
        if num_i == 0:
            num_i = i + 1

        nums[i], nums[j] = num_j, num_i

    return nums[-k:]

if __name__ == '__main__':
    import sys
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    for i in k_uniq_rand_nums_of_n(n, k):
        print i
        
