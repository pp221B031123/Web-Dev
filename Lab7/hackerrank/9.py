if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort(reverse=True)
    for x in arr:
        if x != arr[0]:
            print(x)
            break