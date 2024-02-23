from typing import List

# 1 2 3 4 5 
# n = 5

def sort(arr: List[int]) -> List[int]:
    N = max(arr)
    freq_arr = [0] * (N + 1)
    
    #create a freq array
    for elem in arr:
        freq_arr[elem] += 1    
    
    #convert the freq arr into a prefix sum
    for i in range(1, len(freq_arr)):
        freq_arr[i] += freq_arr[i - 1]

    ans = [-1] * len(arr)

    for elem in arr:
        index = freq_arr[elem] - 1
        if index >= 0:
            ans[index] = elem
    
    for i in range(len(ans) - 1, -1, -1):
        if ans[i] == -1:
            ans[i] = ans[i + 1]

    return ans

def main():
    arr = [5, 9, 1, 55, 0, 4, 60, 59, 100, 100, 0]
    print(sort(arr))

if __name__ == "__main__":
    main()