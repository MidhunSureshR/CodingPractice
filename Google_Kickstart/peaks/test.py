def getPeakCount(height):
    count = 0
    for i in range(1,len(height) - 1):
        if height[i] > height[i-1] and height[i] > height[i+1]:
            count = count + 1
    return count
    
T = int(input())
for i in range(1,T+1):
    N = int(input())
    height = input().split(" ")
    height = [int(x) for x in height]
    count = getPeakCount(height)
    print('Case #{}: {}'.format(i,count))
    

