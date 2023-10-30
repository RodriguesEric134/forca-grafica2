import random
import tkinter as tk
from tkinter import messagebox

# Lista de palavras para o jogo
palavras = ["python", "forca", "programacao", "jogos", "computador", "aprendizado"]

# Inicialização da interface gráfica
root = tk.Tk()
root.title("Jogo da Forca")

# Escolha aleatória de uma palavra
palavra = random.choice(palavras)
letras_adivinhadas = []

# Número máximo de tentativas
max_tentativas = 6

# Função para atualizar a exibição da palavra oculta
def atualizar_palavra():
    resultado = ""
    for letra in palavra:
        if letra in letras_adivinhadas:
            resultado += letra
        else:
            resultado += "_"
    palavra_label.config(text=resultado)

# Função para adivinhar uma letra
def adivinhar_letra():
    letra = letra_entry.get().lower()
    letra_entry.delete(0, tk.END)

    if letra in letras_adivinhadas:
        messagebox.showinfo("Aviso", "Você já adivinhou essa letra.")
    else:
        letras_adivinhadas.append(letra)
        atualizar_palavra()
        if letra not in palavra:
            tentativas_restantes()
            if max_tentativas == 0:
                messagebox.showinfo("Fim de Jogo", f"Você perdeu! A palavra era: {palavra}")
                root.destroy()

    if palavra_label.cget("text") == palavra:
        messagebox.showinfo("Fim de Jogo", f"Parabéns, você venceu! A palavra era: {palavra}")
        root.destroy()

# Função para atualizar o rótulo de tentativas restantes
def tentativas_restantes():
    global max_tentativas
    max_tentativas -= 1
    tentativas_label.config(text=f"Tentativas restantes: {max_tentativas}")

# Interface gráfica
palavra_label = tk.Label(root, text="", font=("Arial", 24))
palavra_label.pack()

letra_entry = tk.Entry(root, font=("Arial", 16))
letra_entry.pack()

adivinhar_button = tk.Button(root, text="Adivinhar Letra", command=adivinhar_letra, font=("Arial", 16))
adivinhar_button.pack()

tentativas_label = tk.Label(root, text=f"Tentativas restantes: {max_tentativas}", font=("Arial", 16))
tentativas_label.pack()

atualizar_palavra()

root.mainloop()
