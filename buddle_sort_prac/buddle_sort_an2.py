
def buddle_sort_2(li):
    n=len(li)
    for i in range(1,n):
        status = False
        for j in range(n-i):
            if li[j]>li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                status = True
        if not status:
            return li
    return li

if __name__ == '__main__':
    li=[1,3,2,5,5,1,5,8,9,0]
    buddle_sort_2(li)
    print(li)