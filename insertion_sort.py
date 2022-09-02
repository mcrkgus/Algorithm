#best : n
#avg : n^2
#worst : n^2

def insertion_sort(arr) :
    for end in range(1, len(arr)) :
        for i in range(end, 0, -1) :
            if(arr[i-1] > arr[i]) :
                arr[i-1], arr[i] = arr[i], arr[i-1]
