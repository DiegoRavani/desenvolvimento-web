def decifrar_mensagem(mensagem):
    if not mensagem:
        return ""
    else:
        primeiro_caractere = mensagem[0]
        if primeiro_caractere == 'z':
            primeiro_caractere = 'a'
        elif 'a' <= primeiro_caractere <= 'y':
            primeiro_caractere = chr(ord(primeiro_caractere) + 1)
        elif 'A' <= primeiro_caractere <= 'Y':
            primeiro_caractere = chr(ord(primeiro_caractere) + 1)
        return primeiro_caractere + decifrar_mensagem(mensagem[1:])

mensagem_codificada = "abc"
print("Mensagem decodificada:", decifrar_mensagem(mensagem_codificada))
