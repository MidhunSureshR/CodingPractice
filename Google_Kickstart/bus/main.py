def getFarthestDay(X, N, D):
    trip_upper = D
    answer = list()
    for trip in X[::-1]:
        # What is the maximum that I can delay the last trip?
        last_possible_day = (trip_upper // trip) * trip
        answer.append(last_possible_day)
        trip_upper = last_possible_day
        # Now that I've delayed the last trip maximally,
        # the problem is reduced by 1 and and D = last_possible_day
    return answer.pop()


T = int(input())
for i in range(1, T+1):
    N, D = [int(x) for x in input().split(" ")]
    X = [int(x) for x in input().split(" ")]
    print('Case #{}: {}'.format(i, getFarthestDay(X, N, D)))
