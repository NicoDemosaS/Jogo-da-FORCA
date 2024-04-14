def receber_letra():  # CORRIGIR ERROS INPUT DA LETRA
    letra = input('Letra: ').upper()
    
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
   
    letra.strip()
    
    if len(letra) > 1:
        print('Erro, letra > 1')
        receber_letra()
        
    if letra not in alfabeto:
        print('Letra nao esta no alfabeto')
        receber_letra()
        
    return letra

letra = receber_letra()
print(letra)