if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        r, c = [int(a) for a in str(input()).split(" ")]
        out = ''
        for j in range(r):
            if j == 0:
                out += f"..{'+-' * (c - 1)}+\n"
                out += f"..{'|.' * (c - 1)}|\n"
            else:
                out += f"{'+-' * c}+\n"
                out += f"{'|.' * c}|\n"
        out += f"{'+-' * c}+\n"
        print(f"Case #{i}:")
        print(out, end='')
