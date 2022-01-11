"""Contar Caracter"""

def contarcaracter(var):
    ordenado = sorted(var)
    ponteiro = ordenado[0]
    contador = 0
    recebedor = {ordenado[0]:contador}
    for var in ordenado[0:]:
       if ponteiro == var:
        contador+=1
        recebedor[ponteiro] = [contador]
       else:
        recebedor[ponteiro] = [contador]
        ponteiro = var
        contador = 1

    print(recebedor)


def contarcaracter_2(v):
    resultado={}
    for caracter in v:
        contagem = resultado.get(caracter,0)
        contagem+=1
        resultado[caracter] = contagem

        return resultado

if __name__ == '__main__':
    print('Dentro do Modulo')
    contarcaracter('wellliakianeyyedoimiduanwdeonaaaatcuuuuuuuuuuu'
                   'uuucrtwxerxrewxrewzrezwrzwzwrrwwzewremommmuoniuonuuoiu')



