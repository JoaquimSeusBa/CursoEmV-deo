c = 'Desafio10'
print(f'{c:=^20}')
n = int(input('Qual tabuada? '))
i = 0
while i <= 10:
    print(f'{n} X {i} = {n * i}')
    i = i + 1
