def main():
    T = int(input())
    for i in range(T):
        N, K = [int(x) for x in input().split(" ")]
        array = [int(x) for x in input().split(" ")]
        
        num_kcountdown = 0
        c = 0
        for j in range(1, len(array)):
            if array[j] == array[j-1]-1:
                c = c+1
            else:
                c = 0
            if array[j] == 1 and c >= K-1:
                num_kcountdown = num_kcountdown+1
                
        print('Case #' + str(i+1) + ': ' +  str(num_kcountdown))


main()