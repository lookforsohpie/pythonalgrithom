fiblist = []
fiblist.append(0)
fiblist.append(1)


def fibstore(n):
    if n < len(fiblist):
        return fiblist[n]
    else:
        fiblist.append(fibstore(n - 1) + fibstore(n - 2))
        return fiblist[n]


def fibiterior(n):
    if n < 2:
        return n
    else:
        n_1 = 0
        n_2 = 1
        sum = 0
        for i in range(n):
            sum = n_1 + n_2
            n_2 = n_1
            n_1 = sum
        return sum


def fib(n):
    if 2 > n:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


num = int(input("How many fibnaqi numbers do you want to show ? \n"))

for i in range(num):
    print(str(i + 1) + "     " + str(fibstore(i)))
for i in range(num):
    print(str(i + 1) + "     " + str(fibiterior(i)))
for i in range(num):
    print(str(i + 1) + "     " + str(fib(i)))