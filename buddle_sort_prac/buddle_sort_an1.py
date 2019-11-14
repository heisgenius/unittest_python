
def buddle_sort(li):
    n=len(li)
    for i in  range(1,n):
        for j in range(n-i):
            if li[j]>li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
    return li
if __name__ == '__main__':
    li=[2,3,4,1,6,8,9,]
    buddle_sort(li)
    print(li)