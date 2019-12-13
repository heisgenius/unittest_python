def buddle_sort_1213(nums):
    n = len(nums)
    for i in range(n-1):
        status = False
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                status = True
        if not status:
            return nums
    return nums

if __name__ == '__main__':

    nums=[1,2,3,5,4,8,9,200,100,-5]
    print('排序前的数列为{}'.format(nums))
    buddle_sort_1213(nums)
    print('排序后的数列为{}'.format(nums))