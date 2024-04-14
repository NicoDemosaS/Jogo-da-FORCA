from random import randint
palavras = ['panaca']

def gerar_palavra():
    randnum = randint(0, len(palavras)-1)
    return palavras[randnum]

palavra_escolhida = gerar_palavra()

cont = 0 


def achar_posicao(letra, palavra_escolhida):
    cont = 0 
    letras_escontradas = []
    for ltr in palavra_escolhida:
        posicao = ltr.find(letra)
        cont += 1 
        if posicao != -1:
            letras_escontradas.append(cont-1) 
    return letras_escontradas
        
palavra_secreta = len(palavra_escolhida) * '-'
lista_secreta = list(palavra_secreta)
lista_secreta[3] = 'C'
print(lista_secreta)