"""Write a program that has a function called write(), that receives any text as a parameter and displays
a message with an adaptable size."""


def write(txt):
    x = '~'
    while len(x) < len(txt)+4:
        x += '~'
    print(x)
    print(f'  {txt}')
    print(x)


write('Vitor Renan de Almeida')
write('Curso de Python no YouTube')
write('CeV')
