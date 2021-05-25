def swap(a, b, arr):
    if a != b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp


def partition1(start, end, ele):
    pivot_ind = end
    pivot_Val = ele[pivot_ind]
    i =start
    while i < end:
        while start < len(ele) and ele[start] < pivot_Val:
            start = start + 1
        i = start
        while i < len(ele) and ele[i] > pivot_Val:
            i = i + 1
        if i < end:
            swap(start, i, ele)



    swap(start,pivot_ind,ele)
    return start

def quick(start,end,ele):

    sp = partition1(start,end,ele)
    if sp == end:
        return ele
    quick(sp+1,end,ele)






if __name__ == "__main__":
    ele = [11, 9, 15 , 2,29, 28, 7]
    start = 0
    end = len(ele) - 1

    quick(start, end,ele)
    print(ele)