juros_simples = lambda C, n, i: (C*n) *i



def sequencia_incognita(lista):
    return lista[0], lista[1], lista[2]




coeficiente = ['C = Capital Inicial','n = Tempo/Prazo(ano)','i = Taxa de Juros']
pergunta = [f'Declare o valor de {c}:' for c in coeficiente]


if __name__ == "__main__":

    sequencia = [float(input(p)) for p in pergunta]
    c,n,i = sequencia_incognita(sequencia)
    valor = juros_simples(c, n, i)
    
    print(valor)
    