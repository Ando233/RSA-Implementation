import random

cnt = [0, 0, 0, 0, 0, 0]
for _ in range(100):
    a = random.randrange(2, 5)
    cnt[a] += 1

print(cnt)