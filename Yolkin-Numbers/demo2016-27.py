N = int(input())
# считываем в очередь первые 6 чисел
Q = [int(input()) for i in range(6)]
for i in range(N-6):
    # первый эл-т покидает очередь и соревнуется с текущими минимальными
    x = Q[0]
    min_x = min(min_x, x)
    if x%2 == 0 and x < min_even:
        min_even = x
    x = int(input())
    beta = min(beta, x*min_even)
    if x%2 == 0:
        beta = min(beta, x*min_x)
    # поэлем-ый сдвиг очереди
    Q.pop(0)
    Q.append(x)