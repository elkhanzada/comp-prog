if __name__ == '__main__':
    numbers = [int(a) for a in str(input()).split(" ")]
    rep = {}
    for n in numbers:
        if n in rep.keys():
            rep[n] += 1
        else:
            rep[n] = 0
    print(max(rep.values()))
