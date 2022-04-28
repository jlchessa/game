import random


palavras = ['DEUS', 'JESUS', 'ESPIRITO SANTO', 'GRAÇA', 'SALVAÇAO', 'CORDEIRO', 'PECADO']

dicas = ['Ele é o criador de todas as coisas', 'Ele é o Filho de Deus', 'Ele é o consolador que foi enviado por Jesus',
         'Jesus nos deu ela atráves da sua crucificação', 'Só vem por meio da fé em Jesus',
         'Jesus morreu como um para nos salvar', 'É aquilo que nos afasta de Deus']
dig = []
tentativas = 5

palavra_secreta = random.choice(palavras)
dica_position = list.index(palavras, palavra_secreta)
dica = dicas[dica_position]
print(f'Bem vindos ao jogo! Você precisa advinhar a PALAVRA SECRETA! '
      f'\n\nNão se preocupe! Vou te dar uma dica.'
      f'\nA dica é a seguinte:\n{dica}')

while True:
    letra = input('\nDigite uma letra: ')
    if letra == letra.lower():
        letra = letra.upper()
        for c in palavra_secreta:
            if c == 'Ç' and letra == 'C':
                print('Troque C por Ç')

    if len(letra) > 1:
        print('Você só pode digitar uma letra!!!')
        continue
    dig.append(letra)

    if letra in palavra_secreta:
        for espaco in palavra_secreta:
            if espaco == ' ':
                palavra_secreta = 'ESPIRITOSANTO'



        print(f'A letra {letra} existe na palavra secreta!')
        print(f'As letras que já foram digitadas são: {dig}')
    else:
        tentativas -= 1
        print(f'A letra {letra} não faz parte da palavra secreta!!!')
        print(f'Você tem {tentativas} tentativas restantes')
        if tentativas <= 0:
            print('Game Over!')
            break
        print(f'As letras que já foram digitadas são: {dig}')


    secreta_temporaria = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in dig:
            secreta_temporaria += letra_secreta
        else:
            secreta_temporaria += '*'
    if secreta_temporaria == palavra_secreta:
        if palavra_secreta == 'ESPIRITOSANTO':
            palavra_secreta = 'ESPIRITO SANTO'
        print('Parabéns!! Você descobriu a palavra secreta!!!\nA palavra secreta era: {}'.format(palavra_secreta))
        break


    print(secreta_temporaria)




