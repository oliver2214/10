from f import f as fun

x = int(input())

for i in range(x+1):
    print(f'f({i}) = {fun(i)}')
