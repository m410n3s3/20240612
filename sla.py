import tkinter as tk
import random
import time

# Configurações da janela principal
janela = tk.Tk()
janela.title("Jogo de Clique")
janela.geometry("600x400")

# Variáveis globais
pontos = 0
tempo_restante = 30  # 30 segundos para o jogo

# Função para resetar os pontos
def resetar_pontos():
    global pontos
    pontos = 0
    pontos_label.config(text=f"Pontos: {pontos}")

# Função para atualizar os pontos e mover o círculo
def clicar(event):
    global pontos
    x, y = event.x, event.y
    x0, y0, x1, y1 = canvas.coords(circulo)
    if x0 <= x <= x1 and y0 <= y <= y1:
        pontos += 1
        pontos_label.config(text=f"Pontos: {pontos}")
        mover_circulo()
    else:
        resetar_pontos()

# Função para mover o círculo para uma nova posição aleatória
def mover_circulo():
    x = random.randint(50, 550)
    y = random.randint(50, 350)
    canvas.coords(circulo, x-20, y-20, x+20, y+20)

# Função para atualizar o tempo
def atualizar_tempo():
    global tempo_restante
    if tempo_restante > 0:
        tempo_restante -= 1
        tempo_label.config(text=f"Tempo restante: {tempo_restante}s")
        janela.after(1000, atualizar_tempo)
    else:
        mostrar_resultado()

# Função para mostrar o resultado final
def mostrar_resultado():
    if pontos >= 10:
        mensagem = f"Incrível! Você conseguiu {pontos} pontos! Conquista: Mestre dos Cliques"
    elif pontos >= 5:
        mensagem = f"Bom trabalho! Você conseguiu {pontos} pontos! Conquista: Clicker Expert"
    else:
        mensagem = f"Você conseguiu {pontos} pontos. Tente novamente para melhorar!"

    resultado_label.config(text=mensagem)

# Cria um canvas para desenhar
canvas = tk.Canvas(janela, width=600, height=400)
canvas.pack()

# Cria o círculo inicial
x_inicial = random.randint(50, 550)
y_inicial = random.randint(50, 350)
circulo = canvas.create_oval(x_inicial-20, y_inicial-20, x_inicial+20, y_inicial+20, fill="blue")

# Adiciona evento de clique ao canvas
canvas.bind("<Button-1>", clicar)

# Labels para mostrar os pontos e o tempo
pontos_label = tk.Label(janela, text=f"Pontos: {pontos}", font=("Helvetica", 16))
pontos_label.pack()

tempo_label = tk.Label(janela, text=f"Tempo restante: {tempo_restante}s", font=("Helvetica", 16))
tempo_label.pack()

resultado_label = tk.Label(janela, text="", font=("Helvetica", 16))
resultado_label.pack()

# Inicia o timer
janela.after(1000, atualizar_tempo)

# Inicia o loop principal da interface gráfica
janela.mainloop()
