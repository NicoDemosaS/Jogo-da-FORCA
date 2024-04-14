from random import randint

palavras = ['cacto']

letras_digitadas = []

def gerar_palavra():
    randnum = randint(0, len(palavras)-1)
    return palavras[randnum]

def achar_posicao(letra, palavra_escolhida):
    cont = 0 
    letras_escontradas = []
    for ltr in palavra_escolhida:
        posicao = ltr.find(letra)
        cont += 1 
        if posicao != -1:
            letras_escontradas.append(cont-1) 
    return letras_escontradas

def receber_letra():
    pass
        
        
        
        
        
def main():
    numero_de_vidas = 5
    palavra_escolhida = gerar_palavra()
    palavra_secreta = len(palavra_escolhida) * '-'
    lista_secreta = list(palavra_secreta)
    
    print('Iniciando jogo')

    while True:

        print(lista_secreta)
        letra = input("Letra: ")
        
        if len(letra) > 1:
            print('PORFAVOR DIGITE SO UMA LETRA..')
        
        
        elif letra in letras_digitadas:
            print(f'LETRA JÁ DIGITADA')
            
        elif letra not in letras_digitadas:
            letras_digitadas.append(letra)
            
            if letra in palavra_escolhida:
                print(f'Letra correta! {letra}')
                posicoes = achar_posicao(letra, palavra_escolhida)

                for posicao in posicoes:
                    lista_secreta[posicao] = letra
                                 
            if letra not in palavra_escolhida:
                print(f'Letra incorreta {letra}')
                numero_de_vidas -= 1
                print(f'Voce perdeu uma vida! vidas restantes: {numero_de_vidas}')
                    
            print(f'Letras digitadas : {letras_digitadas}')
         
        elif '-' not in lista_secreta:
            print(lista_secreta)
            break
                
        elif numero_de_vidas == 0:
            print(f'Voce perdeu! a palavra era >{palavra_escolhida.upper()}<')
            break

if __name__ == '__main__':
    main()