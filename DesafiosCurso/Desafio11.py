c = 'Desafio11'
print(f'{c:=^20}')
l = int(input('Qual a largura da parede? '))
a = int(input('Qual a altura da parede? '))
if (l*a%2)==0:
    print(f'Serão necessários {l*a//2} litros de tinta')
else: print(f'Serão necessários {l*a//2+1} litros de tinta')