# 2024-04-16 알고리즘 공부(Studying Algorithm)
# 배운내용 토대로 스스로 큐 구현해보기
queue = list()
size = 0

def s_append(s, data):
    global size
    s.append(data)
    size += 1

def s_popleft(s):
    global size
    try:
        tmp = s[0]
        s.remove(s[0])
        size -= 1
        return tmp
    except IndexError:
        print("There's no more data in queue.")

while True:
    print("0. close\n1. append\n2. popleft\n3. print")
    try:
        tc = int(input(">>> "))
        if tc == 1:
            val = int(input(">>> "))
            s_append(queue, val)
            print("complete.")
        elif tc == 2:
            print(s_popleft(queue))
            print("complete.")
        elif tc == 3:
            print(queue)
            print("complete.")
        elif tc == 0:
            print("Done.")
            break
        else:
            print("Try again.")
    except ValueError:
        print("Try again.")