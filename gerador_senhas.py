from tkinter import *
from tkinter import ttk
from random import randint, shuffle
import pyperclip

########## INFORMAÇÕES ##########
# Título: Gerador de senhas
# Autor: Alysson Estevam
# Data: 11/03/2024
# Última alteração: 11/03/2024

# Para usar o pyperclip
# pip install pyperclip

# Para gerar o executável
# pip install pyinstaller
# cd D:\automacao\scripts_python
# pyinstaller --onefile --noconsole gerador_senhas.py

# A-Z : 65-90
# a-z : 97-122
# 0-9 : 48-57                                                           
# Caracteres especiais : 33, 35, 36, 37, 38, 42, 43, 45, 63, 64, 94, 95 
# Caracteres oracle: 35 (#), 45 (-), 95 (_)                             
                                                                 
# print('Maiusculas:',len(lista_maiusculas))                            
# print('Minusculas:',len(lista_minusculas))                            
# print('Numeros:',len(lista_numeros))                                  
# print('Especiais:',len(lista_especiais))                              
# print('Especiais Oracle:',len(lista_especiais_oracle))                
# print('Geral:',len(lista_geral))                                      
# print('Geral Oracle:',len(lista_geral_oracle))                        

# Cores
cor_preto = "#1e1f1e"
cor_branco = "#feffff"
cor_vermelho = "#EC0033"
cor_laranja = "#FFAB40"

# Define as listas de caracteres para o sorteio
lista_maiusculas = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]
lista_minusculas = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
lista_numeros = [48,49,50,51,52,53,54,55,56,57]
lista_especiais = [33,35,36,37,38,42,43,45,63,64,94,95]
lista_especiais_oracle = [35,45,95]
lista_geral = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,48,49,50,51,52,53,54,55,56,57,33,35,36,37,38,42,43,45,63,64,94,95]
lista_geral_oracle = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,48,49,50,51,52,53,54,55,56,57,35,45,95]

janela = Tk()
janela.title("GERADOR DE SENHAS")
janela.resizable(False, False)

# Definindo as dimensões da janela largura x cumprimento
janela.geometry("700x360")

# Criando frames
frame_corpo = Frame(janela, 
                    width=700, 
                    height=360, 
                    bg=cor_preto)
frame_corpo.grid(row=1, 
                 column=0)

#Criando Label
valor_label_titulo = StringVar()

valor_label_titulo.set('GERADOR DE SENHAS')

titulo_label = Label(frame_corpo, 
                  textvariable=valor_label_titulo, 
                  height=2, 
                  relief=FLAT, 
                  anchor="e", 
                  justify=CENTER, 
                  font='Verdana 20 bold', 
                  fg=cor_branco, 
                  bg=cor_preto)
titulo_label.place(relx=0.5, 
                y=50, 
                anchor=CENTER)

label_quantidade_caracteres = Label(frame_corpo, text='Caracteres: ',
                       font='Verdana 15 bold',
                       bg=cor_preto,
                       fg=cor_branco)
label_quantidade_caracteres.place(relx=0.44,
                 y=100,
                 anchor=CENTER)
# Spinbox
quantidade_caracteres = StringVar(value=8)
spin_box = ttk.Spinbox(
    frame_corpo,
    from_=8,
    to=30,
    textvariable=quantidade_caracteres,
    wrap=False,
    width=5,
    font='Verdana 12 bold')
spin_box.place(relx=0.59,
               y=102,
               anchor=CENTER)

# Senha gerada
txt_senha = Text(frame_corpo, height=1,
                    width=35,
                    bg=cor_branco,
                    font='Verdana 15 bold')
txt_senha.place(relx=0.5,
                y=160,
                anchor=CENTER)
txt_senha.tag_configure("center", justify='center')
txt_senha.insert("1.0", "******************************")
txt_senha.tag_add("center", "1.0", "end")
txt_senha.config(state=DISABLED)

def copiar_senha():
    senha = txt_senha.get('1.0', END)
    pyperclip.copy(senha)

botao_copiar = Button(frame_corpo, command=copiar_senha, text="COPIAR", width=10, height=2, bg=cor_branco, font='Verdana 6 bold', relief=RAISED, overrelief=RIDGE)
botao_copiar.place(relx=0.92,
                        y=160,
                        anchor=CENTER)

def gerar_senha(tipo_senha):
    global spin_box
    quantidade_caracteres = int(spin_box.get())

    if quantidade_caracteres < 8:
        quantidade_caracteres = 8

    senha = ''

    # Gera 2 letras maiúsculas
    index = randint(0,25)
    senha += chr(lista_maiusculas[index])
    index = randint(0,25)
    senha += chr(lista_maiusculas[index])

    # Gera 2 letras minúsculas
    index = randint(0,25)
    senha += chr(lista_minusculas[index])
    index = randint(0,25)
    senha += chr(lista_minusculas[index])

    # Gera 2 números
    index = randint(0,9)
    senha += chr(lista_numeros[index])
    index = randint(0,9)
    senha += chr(lista_numeros[index])

    if tipo_senha == 'S':
        # Gera 2 caracteres especiais para o Oracle
        index = randint(0,2)
        senha += chr(lista_especiais_oracle[index])
        index = randint(0,2)
        senha += chr(lista_especiais_oracle[index])
    else:
        # Gera 2 caracteres especiais para os demais tipos de senha
        index = randint(0,11)
        senha += chr(lista_especiais[index])
        index = randint(0,11)
        senha += chr(lista_especiais[index])

    # Continua a geração da senha caso seja maior que 8 caracteres
    for i in range(1, quantidade_caracteres-7):
        if tipo_senha == 'S':
            index = randint(0,64)
            senha += chr(lista_geral_oracle[index])
        else:
            index = randint(0,73)
            senha += chr(lista_geral[index])

    lista_senha = list(senha)
    shuffle(lista_senha)

    txt_senha.config(state=NORMAL)
    txt_senha.delete('1.0', END)
    txt_senha.insert('1.0', ''.join(lista_senha))
    txt_senha.tag_add('center', '1.0', 'end')
    txt_senha.config(state=DISABLED)

# Criando botões
# place = posição do botão em coordenadas x, y.
botao_gerar_senha = Button(frame_corpo, command=lambda: gerar_senha('N'), text="GERAR SENHA", width=20, height=2, bg=cor_laranja, font='Verdana 13 bold', relief=RAISED, overrelief=RIDGE)
botao_gerar_senha.place(relx=0.5,
                        y=220,
                        anchor=CENTER)

botao_gerar_senha_oracle = Button(frame_corpo, command=lambda: gerar_senha('S'), text="GERAR SENHA ORACLE", width=20, height=2, bg=cor_vermelho, font='Verdana 13 bold', relief=RAISED, overrelief=RIDGE)
botao_gerar_senha_oracle.place(relx=0.5,
                        y=290,
                        anchor=CENTER)

janela.mainloop()
