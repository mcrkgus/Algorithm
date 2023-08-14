def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # 원하는 값의 인덱스 반환
    return -1  # 원하는 값이 없을 경우 -1 반환


my_list = [3, 8, 12, 5, 2, 9, 17]
target = 5

result = linear_search(my_list, target)

if result != -1:
    print(f"찾는 값 {target}은 인덱스 {result}에 위치합니다.")
else:
    print(f"찾는 값 {target}을 찾을 수 없습니다.")
