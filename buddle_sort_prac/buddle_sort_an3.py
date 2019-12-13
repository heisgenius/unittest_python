def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):  # 这个循环负责设置冒泡排序进行的次数
        status = False

        for j in range(n - i - 1):  # j为列表下标,为什么里面的循环判断条件是j>n-i-1呢？这要从冒泡排序原理说起：冒泡排序每循环一次,就把最大的数排在了最右边（不信你试试），所以下次循环的时候就不用再循环这么多个啦，只需要循环n-i次；至于为什么还要-1，是因为j从0开始的
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                status = True
        if not status:
            return nums
    return nums

if __name__ == '__main__':
    nums=[5,3,1,4,6,3,7,0,90,4343,3,6,-3]
    bubble_sort(nums)
    print(nums)