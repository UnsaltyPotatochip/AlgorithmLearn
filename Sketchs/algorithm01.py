# 2024-03-16 알고리즘 공부(Studying Algorithm)
import random
findNumber = random.randrange(1, 101)

for i in range(1, 101):
    if i == findNumber:
        print(i)
        break
