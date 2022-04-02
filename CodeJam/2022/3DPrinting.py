if __name__ == '__main__':
    n = int(input())
    for t in range(1, n + 1):
        printers = []
        for i in range(3):
            printers.append([int(a) for a in str(input()).split(' ')])
        print(f"Case #{t}: ", end='')
        mins = [min(list(zip(*printers))[b]) for b in range(4)]
        if sum(mins) < 1_000_000:
            print("IMPOSSIBLE")
            continue
        for colors in printers:
            if sum(colors) < 1_000_000:
                print("IMPOSSIBLE")
                break
        else:
            diff = sum(mins) - 1_000_000
            final = []
            for i in range(len(mins)):
                if diff > mins[i]:
                    final.append(0)
                    diff -= mins[i]
                else:
                    final.append(mins[i] - diff)
                    diff = 0
            print(*final)
