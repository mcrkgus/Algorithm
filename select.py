#평균 선형 시간 선택 알고리즘 select

def select(a, p, r, i):     #배열 a[p~r]에서 i번째 작은 원소 찾기 
    if p==r:
        return a[p]
    
    q = partition(a, p, r)
    k = q-p+1
    
    if i<k:
        return select(a, p, q-1, i)
    elif i==k:
        return a[q]
    else:
        return select(a, q+1, r, i-k)
    
def partition(a, p, r):
    pivot = a[r]
    i = p-1
    for j in range(p, r):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    
    a[r], a[i+1] = a[i+1], a[r]
    
    return i+1
