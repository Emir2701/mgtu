def nice_print(arr):
    n = len(arr)
    
    count_str = 0
    while  2**count_str <= n:
        count_str += 1
    i_0 = 0
    for i in range(count_str):
        print(*arr[i_0: i_0 + 2**i ])
        i_0 += 2**i
    print()

arr = [1, 2, 3, 4]
nice_print(arr)