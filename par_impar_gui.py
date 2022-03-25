# Jogo do par ou ímpar
# Jogo contra a máquina no qual a máquina sorteia um número, o usuário escolhe par ou ímpar e descobre se acertou

import tkinter as tk
import random


def sortear_valor():
    return random.randint(1, 10)


def verifica_resposta():
    maquina = sortear_valor()
    if (maquina % 2 == 0 and var_numero.get() == "p") or (maquina % 2 != 0 and var_numero.get() == "i"):
        resultado["text"] = f"Parabéns, você acertou! O número escolhido pela máquina foi {maquina}."
    elif (maquina % 2 == 0 and var_numero.get() == "i") or (maquina % 2 != 0 and var_numero.get() == "p"):
        resultado["text"] = f"Você errou... O número escolhido pela máquina foi {maquina}."
    else:
        resultado["text"] = "Por favor escolha Par ou Ímpar antes de enviar o palpite."


###CONSTRUÇÃO DA INTERFACE###

janela = tk.Tk()
janela.title("Jogo do par ou ímpar")
janela.resizable(False, False)


titulo = tk.Label(text="Jogo do par ou ímpar", padx=10, pady=10, bg="black", fg="white", font=("Montserrat", 20), width=50, height=5)
titulo.grid(row=0, column=0, columnspan=4)

instrucao = tk.Label(text="A máquina escolheu um número inteiro entre 1 e 10. Você acha que é par ou ímpar?", padx=10, pady=15, font="Montserrat", width=80, height=3)
instrucao.grid(row=2, column=0, columnspan=4, rowspan=2)

var_numero = tk.StringVar(value="nada")

par = tk.Radiobutton(text="Par", variable=var_numero, value="p", pady=25, font="Montserrat")
par.grid(row=4, column=1)

impar = tk.Radiobutton(text="Ímpar", variable=var_numero, value="i", pady=25, font="Montserrat")
impar.grid(row=4, column=2)

enviar = tk.Button(text="Enviar palpite", command=verifica_resposta, pady=10, font="Montserrat", bg="gray", activebackground="white")
enviar.grid(row=5, column=1, columnspan=2, ipadx=20)

resultado = tk.Label(text="", padx=10, pady=20, font="Montserrat")
resultado.grid(row=6, column=0, columnspan=4)

janela.mainloop()

