


def bubble_sort(the_list):
    i = 0
    while i < len(the_list):
        j = 0
        status = False
        while j < len(the_list) - 1:
            # print(the_list[j], the_list[j + 1])
            if the_list[j] > the_list[j + 1]:
                the_list[j], the_list[j + 1] = the_list[j + 1], the_list[j]
            j = j + 1
            status = True
        if not status:
            return the_list
            # print(the_list)

        # print("======" + str(the_list))

        i = i + 1
    return the_list


if __name__ == '__main__':
    the_list = [1, 2, 767, 4, 5, 6, 7, 8, 9, 10]
    print("排序前：" + str(the_list))

    print("排序后：" + str(bubble_sort(the_list)))
