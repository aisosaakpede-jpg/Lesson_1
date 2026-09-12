def double_loop_steps(n):
    steps = 0
    for i in range(1,n + 1):
        for j in range(i):
            steps += 1
    return steps
values = [4, 10, 100, 1000]
for n in values:
    steps = double_loop_steps(n)
    print("n = ", n)
    print("Steps = ",steps)
    print()