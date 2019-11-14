def bubble_sort(nums):
    for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数
        status = False
        for j in range(len(nums) - i - 1):  # j为列表下标
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