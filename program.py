from f import f as fun

x = int(input())


s = f'f({x}) = {fun(x)}'

print(s[::-1])