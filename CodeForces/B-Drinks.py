if __name__ == '__main__':
    n = int(input())
    percents = [int(a) for a in str(input()).split(" ")]
    print(sum(percents) / (n * 100) * 100)
