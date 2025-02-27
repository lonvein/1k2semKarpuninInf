def max_meetings(N, start, end):
    meetings = list(zip(start, end))
    meetings.sort(key=lambda x: x[1])
    count = 1
    last_end = meetings[0][1]
    for i in range(1, N):
        if meetings[i][0] >= last_end:
            count += 1
            last_end = meetings[i][1]
    return count
N = int(input())
start = list(map(int, input().split()))
end = list(map(int, input().split()))
print(max_meetings(N, start, end))