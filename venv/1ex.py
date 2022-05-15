import numpy as np
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return nums
def define_eps32():
    j=1
    i=1
    exp=0
    while (j>0):
        if (np.float32(1+1/(2**i))-np.float32(1))==0:
            break
        else:
            i+=1
    for k in range(0,32-i):
        exp+=2**k
    eps=np.float32(1+1/(2**(i-1)))-np.float32(1)
    mass=[np.float32(1),np.float32(1+eps/2),np.float32(1+eps),np.float32(1+eps+eps/2)]
    return 'Mantissa discharge-{},UPL-{},max exp-{},min exp-{},comparison-{}'.format(i-1,eps,exp-int((exp+1)/2),-int((exp+1)/2),bubble_sort(mass))
def define_eps64():
    j = 1
    i = 1
    exp=0
    while (j > 0):
        if (np.float64(1 + 1 / (2 ** i)) - np.float64(1)) == 0:
            break
        else:
            i += 1
    for k in range(0,64-i):
        exp+=2**k
    eps=np.float64(1+1/(2**(i-1)))-np.float64(1)
    mass = [np.float64(1), np.float64(1 + eps / 2), np.float64(1 + eps), np.float64(1 + eps + eps / 2)]
    return 'Mantissa discharge-{},UPL-{},max exp-{},min exp-{},comparison-{}'.format(i-1,eps,exp-int((exp+1)/2),-int((exp+1)/2),bubble_sort(mass))
print(define_eps32())
print(define_eps64())
