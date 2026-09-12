values = [4, 10, 100, 1000]
for n in values:
    scores = []
    for i in range(1, n+1):
        scores.append(i)
    print("n = ", n)
    print(("The number of scores stored ="),len(scores))
    print()
