lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
for comida in lanche:
    print(f'Eu vou comer {comida[0:2]}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(5))
print(c.index(5))
print(c.index(5, 1))




