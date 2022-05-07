## ATIVIDADE 1
x = 10+3*3
print(f'Valor: {x}; Tipo: {type(x)}') # x = 19, tipo = int

## ATIVIDADE 2
x = 10+18/2
print(f'Valor: {x}; Tipo: {type(x)}') # x = 19.0, tipo = float

## ATIVIDADE 3
x = 10+18//2-1
print(f'Valor: {x}; Tipo: {type(x)}') # x = 18, tipo = int

## ATIVIDADE 4
x = 1+2*3+40//3%5-2+3*5%2
print(f'Valor: {x}; Tipo: {type(x)}') # x = 9, tipo = int

## ATIVIDADE 5
x = 1+2*3+40/3%5-2+3//2*5
print(f'Valor: {x}; Tipo: {type(x)}') # x = 13.333333333333334, tipo = float

## ATIVIDADE 6
x = 0
for i in range(1, 11):
    x = x + i
print(x) # x = 55

## ATIVIDADE 7
media = (7.7+8.35)/2
print(media) # media = 8.025

## ATIVIDADE 8
n1 = 7
n2 = 9
media_final = (n1*2+n2*3)/5
print(media_final) # media_final = 8.2

## ATIVIDADE 9
x = '73623'
m = 1
for i in range(len(x)-(len(x)-1)):
    m = m * 10
digito = int(x)%m
print(digito) # digito = 3

## ATIVIDADE 10
seg = 10000
h = seg//3600
seg = seg%3600
m = seg//60
s = seg%60
print(f'H: {h}, M: {m}, S: {s}') # h = 2, m = 46, s = 40

## ATIVIDADE 11
x = '1234'
x_invertido = x[::-1]
print(int(x_invertido))