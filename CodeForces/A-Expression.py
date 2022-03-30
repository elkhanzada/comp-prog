if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    sm = 0
    if sm < a * b * c:
        sm = a * b * c
    if sm < a + b + c:
        sm = a + b + c
    if sm < a + b * c:
        sm = a + b * c
    if sm < a * b + c:
        sm = a * b + c
    if sm < (a + b) * c:
        sm = (a + b) * c
    if sm < a * (b + c):
        sm = a * (b + c)
    print(sm)
