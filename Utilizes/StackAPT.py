# 2024-04-16 알고리즘 공부(Studying Algorithm)
# 배운내용 토대로 스스로 스택 구현해보기
stack = list()
size = 0

def s_append(s, data):
    global size
    s.append(data)
    size += 1

def s_pop(s):
    try:
        global size
        tmp = s[size-1]
        s.remove(s[size-1])
        size -= 1
        return tmp
    except IndexError:
        print("There's no more data in stack.")

while True:
    print("0. close\n1. append\n2. pop\n3. print")
    try:
        tc = int(input(">>> "))
        if tc == 1:
            val = int(input(">>> "))
            s_append(stack, val)
            print("complete.")
        elif tc == 2:
            print(s_pop(stack))
            print("complete.")
        elif tc == 3:
            print(stack)
            print("complete.")
        elif tc == 0:
            print("Done.")
            break
        else:
            print("Try again.")
    except ValueError:
        print("Try again.")
