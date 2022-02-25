T= int(input())
h = []
food = 0
def feed(i, j, q):
    global h
    global food
    if h[i] - q >= 0 and h[j] - q >= 0:
        h[i] -= q
        h[j] -= q
        food += 2*q
for each in range(T):
    food = 0
    min = 1000000000000000000000
    n = int(input())
    h = list(map(int, input().split()))
    for i,c in enumerate(h):
        if i != n-1:
            if c < min:
                min = c
        if i + 2 <= n - 1:
            if h[i+1] > c:
                feed(i+1, i+2, h[i+1] - h[i])
        #print(h)
    if sum(h) != min*len(h):
        for i, c in enumerate(h):
            if h[-(i+1)] < min:
                min = c
            if n - i -3 >= 0:
                if h[-(i+2)] > h[-(i+1)]:
                    feed(-(i+2), -(i+3), h[-(i+2)] - h[-(i+1)])
            #print(h)

    if sum(h) == min*len(h):
        print(food)
    else:
        print(-1)
