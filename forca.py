import random

# Lista de palavras para o jogo
palavras = ["python", "forca", "programacao", "jogos", "computador", "aprendizado"]

# Escolha aleatória de uma palavra
palavra = random.choice(palavras)

# Lista para acompanhar as letras adivinhadas
letras_adivinhadas = []

# Número máximo de tentativas
max_tentativas = 6

# Função para exibir a palavra oculta com as letras adivinhadas
def exibir_palavra(palavra, letras_adivinhadas):
    resultado = ""
    for letra in palavra:
        if letra in letras_adivinhadas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

# Loop principal do jogo
while True:
    # Exibe a palavra com as letras adivinhadas
    palavra_oculta = exibir_palavra(palavra, letras_adivinhadas)
    print("Palavra: " + palavra_oculta)

    # Solicita ao jogador uma letra
    letra = input("Adivinhe uma letra: ").lower()

    # Verifica se a letra já foi adivinhada
    if letra in letras_adivinhadas:
        print("Você já adivinhou essa letra.")
    else:
        letras_adivinhadas.append(letra)

        # Verifica se a letra está na palavra
        if letra in palavra:
            print("Letra correta!")
        else:
            print("Letra incorreta!")
            max_tentativas -= 1

    # Verifica se o jogador ganhou o jogo
    if palavra_oculta == palavra:
        print("Parabéns, você venceu! A palavra era: " + palavra)
        break

    # Verifica se o jogador perdeu o jogo
    if max_tentativas == 0:
        print("Você perdeu! A palavra era: " + palavra)
        break
