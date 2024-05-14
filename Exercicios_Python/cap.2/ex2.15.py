# Crie um programa que peça ao usuário para digitar uma palavra. O programa deve então indicar se a palavra inserida começa com uma vogal ou uma consoante.

palavra = input("Digite uma palavra: ").lower()

if palavra and palavra[0] in 'aeiou':
    print("A palavra inivia com uma vogal.")
else:
    print("A palavra inicia com uma consoante.")    
