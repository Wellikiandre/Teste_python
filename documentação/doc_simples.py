"""Documentação: Resumo do apresentado no python bird"""
#Variavel e atribuição
#Sempre começar com  : _ ou letra
var=1
#imprimir typo e variavel
print(type(var))
print(var)

#coeficiente divisao
5//2

#resto da divisao
5%2

#elevado / potenciacao
2**3

#separação de milhar
1_000_000

#Ponto flutuante (FLoat)
1.35

#converter para inteiro, ele ignora o decimal
int(0.75)

#ultimo elemento impresso _ type(_)

#soma variavel ++ de c#
n=3
n+=3
n*=3
n*=n

#negacao bool not true, not true

#ou e e(and) , true and true ,false or true

# pergunta >, < , == igual , diferente , está contido
5>6
6<5
6==7
7!=7
1<2 and 4>5
1<4>5

# desvio condicional if
i=3
if i >4:
    i
elif i>6:
    i
else:
    i
#container

#String
'wellik' # mais usual
"wellik" # menos usual

#pular linha '\n' ou # tres'''

#concaternar
'aaa'+'bbb'

#lista de atributos e metodos
dir('')
help(''.lower())

#lista
a=[1,2,3,4,'asd']
a=['ddas',]

#range lista
a=list(range(10))
a=list(range(1,10))
a=list(range(1,10,2))
a=list(range(10,2,-2))

# adicionar list
lista = [1,2,5,3]
lista.append(12)

#ordenar
lista.sort()

#lista retirar o ultimo
lista.pop()

#varios add
lista[1,2]
lista.extend(2,2,341)

#lista concatenar
lista + [2,4,3]

#multiplicar lista
lista *3

#separador retorna lista
'wellikiandre martins'.split()
'wellikiandre-martins'.split('-')

#separar por coringa , ira substituir o '#'.
'#'.join(lista)

# Tupla(), separada por virgula(,)
tlp = (1,2)
tuple(range(6))
tlp = (1,)

#desenpacotar
registro = ('wellik',30)
nome,idade = registro

#funcao id
id(registro)
#id(_)

#acesso a variavel caracter
nome='wellik'
nome[0]
len(nome)
nome[len(nome)-1]
nome[-1]

#fatiamento[inicio:fim:passo]
nome='abcde'
nome[0:3]
nome[-3:]
nome[:3]
nome[::-1] #reverso

#while
nome='abcde'
i=0
while i<len(nome):
    print(nome[i])
    i+=1

#for
nome2='abcde'
for v in nome2:
    print(v)

#for com indice enumaret
#Antigo
nome3='abcde'
for i in range(len(nome3)):
    print(i,nome3[i])

#parte 1 enumerat
for i, v in enumerate(nome3):
    print(i, nome3[i])

#ou
for i, v in enumerate(nome3):
    print(i, v)

#dicionario, mapa ou rachtabel
linguas = {'br':'portuues', 'ing':'ingles'}
linguas['ing']
linguas.get('ing')
linguas.get('ing','não encontrado')
#se existe no mapa
'ing' in linguas
#exemplo list
11 in list[range(20)]


#interação em dicionario
for chave in linguas:
    print(chave)

for chave in linguas.keys():
    print(chave)

for chave in linguas.values():
    print(chave)


for chave in linguas.items():
    print(chave)


for chave,valor in linguas.keys():
    print(chave, valor)

#remover dicionario
linguas.pop('br')
del linguas['br']

#pep 8 (letra minusculas, _)
#funcao

def teste():
    return 'olá'

def teste2():
    pass
#nonotype null


#f string, etiqueta

def ola(n):
    return f'olá {n}'
ola('wellik')

#justa posicao
def ola(n,sobrenome):
    return f'olá {n} {sobrenome}'
ola('wellik','Martins')

#valor default
def ola(n,sobrenome='default teste'):
    return f'olá {n} {sobrenome}'
ola('wellik')
ola('wellik','martins')

# sem ser justa posicao
ola('wellik', sobrenome='teste')


#parametros variaveis
#*args convesao pode ser qualquer coisa
def soma (*args):
    print(args)
    print(type(args))
    aux =0
    for valor in args:
        aux+=valor
    return aux

#parametros nomeados
def f(**kwargs):
    print(kwargs)
    print(type(kwargs))


def f(*args,**kwargs):
    print(*args,**kwargs)
    print(type(*args,**kwargs))

    #desempacotamento
a=(1,2,3)
b = {'ar':12,'i2':213}
f(*a,**b)

#modulo eo script dentro do codigo
#from matematica.mat import soma as s
# help (mat.som)

#Juntar linhas ctrl+shift+J
#alt multiplica cursor
#python wiki org lista de exercicio

#codepen.io



















