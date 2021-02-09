n=5
for i in range(n):
    print(' ' * i, end='')
    print('*'*((n*2)-(i*2+1)))

for i in range(n):
    print(' ' * i + '*' * (2*n-(2*i+1)))