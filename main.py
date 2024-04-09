from random import randint

palavras = ['cacto']

numero_de_vidas = 5
palavra_escolhida = gerar_palavra()
letras_digitadas = []

def gerar_palavra():
    randnum = randint(0, len(palavras)-1)
    return palavras[randnum]
   



def main():
    print('Iniciando jogo')
    while True:
        
        letra = input("Letra: ")
        
        if letra not in letras_digitadas:
            letras_digitadas.append(letra)
            
        if letra not in palavra_escolhida:
            numero_de_vidas -= 1
            print(f'Voce perdeu uma vida! vidas restantes: {numero_de_vidas}')
            
        if numero_de_vidas == 0:
            print(f'Voce perdeu! a palavra era >{palavra_escolhida.upper()}<')
            break

if __name__ == '__main__':
    main()