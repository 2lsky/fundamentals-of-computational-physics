import numpy as np
def bubble_sort(nums,order):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] - nums[i + 1]>0:
                order[i], order[i + 1] = order[i + 1], order[i]
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return nums,order
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
    mass={'1+3*e/2':np.float32(1+3*eps/2),'1+5*e/2':np.float32(1+5*eps/2),'1+e+e/2':np.float32(1+eps+eps/2),'1':np.float32(1)}
    values=list(mass.values())
    order=list(mass.keys())
    return 'Mantissa discharge-{},UPL-{},max exp-{},min exp-{},comparison-{}'.format(i-1,eps,exp-int((exp+1)/2),-int((exp+1)/2),bubble_sort(values,order))
def define_eps64():
    j = 1
    i = 1
    exp=0
    while (j > 0):
        if (float(1 + 1 / (2 ** i)) - float(1)) == 0:
            break
        else:
            i += 1
    for k in range(0,64-i):
        exp+=2**k
    eps=float(1+1/(2**(i-1)))-float(1)
    mass = {'1+3*e/2': np.float64(1+3*eps/2), '1+5*e/2': np.float64(1 + 5*eps/2), '1': np.float64(1),'1+e/2': np.float64(1+eps/2)}
    values = list(mass.values())
    order = list(mass.keys())
    return 'Mantissa discharge-{},UPL-{},max exp-{},min exp-{},comparison-{}'.format(i-1,eps,exp-int((exp+1)/2),-int((exp+1)/2),bubble_sort(values,order))
print(define_eps32())
print(define_eps64())

