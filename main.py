#importando a biblioteca tkinter

from tkinter import *
from tkinter import ttk

#criando janela 

#cores
co1 = "#feffff"
co2 = "#5a5b5c"  
co3 = "#BBBBBB"
co4 = "#12184E"


fundo = "#3b3b3b"

#display

janela = Tk() # Cria a janela principal
janela.title('Calculadora') # Define o titulo da janela
janela.geometry('235x331') # Define tamanho  da janela
icon = PhotoImage(file='calculadora.png')  # Carrega o PNG
janela.iconphoto(False, icon)  # Define ícone usando PNG
janela.configure(bg=fundo) # Define background color
janela.resizable(width=False, height=False)  # Impede redimensionamento

#criando frames

#frame_tela display do resultado
frame_tela = Frame(janela, width=235, height=50, bg=co2) # Cria o frame da tela
frame_tela.grid(row=0, column=0) # Define a posição do frame na janela

#frame_corpo onde ficam os botões
frame_corpo = Frame(janela, width=235, height=280, bg=co1) # Cria o frame do corpo 
frame_corpo.grid(row=1, column=0) # Define a posição do frame na janela

todos_valores = ''  # Variável para armazenar os valores digitados / global para acesso em funções
valor_texto = StringVar()  # Variável para o texto exibido na tela

#criando funções

# função para adicionar valores digitados
def entrar_valores(valor):
    global todos_valores # Acessa a variável global
    todos_valores = todos_valores + str(valor)  # Adiciona o valor digitado à variável

    valor_texto.set(todos_valores)  # Atualiza o texto exibido na tela

# função para calcular o resultado
def calcular():
    global todos_valores  # Acessa a variável global
    try:
        resultado = eval(todos_valores)  # Avalia a expressão matemática
        valor_texto.set(resultado)  # Exibe o resultado na tela
    except Exception as e:
        valor_texto.set("Erro")  # Exibe erro se houver problema na avaliação

# função para limpar a tela
def limpar_tela():
    global todos_valores  # Acessa a variável global
    todos_valores = ''  # Reseta a variável
    valor_texto.set('')  # Limpa o texto exibido na tela

#criando e configurando label para display
app_label = Label(
    frame_tela, # Localização do label no frame_tela
    textvariable = valor_texto, # Usa a variável StringVar para o texto
    width=16,  # Largura do label
    height=2, # Altura do label
    padx=7, # Espaçamento interno horizontal
    relief=FLAT, # Tipo de borda
    bg=co2, # Cor de fundo do label
    fg=co1, # Cor do texto
    font=('Ivy 18 '), # Fonte e tamanho do texto
    anchor='e', # Alinha o texto à direita
    justify=RIGHT) # Justifica o texto à direita
app_label.place(x=0, y=0)  # Posiciona o label no frame_tela

#criando os botões
b_1 = Button(
    frame_corpo, # Localização do botão no frame_corpo
    command=limpar_tela, # Ação ao clicar no botão, chamando a função limpar_tela
    text='C', # Texto exibido no botão
    width=16,  # Largura do botão
    height=3, # Altura do botão
    bg=co1, # Cor de fundo do botão
    font=('Ivy 9 bold'), # Fonte e tamanho do texto
    relief=RAISED, # Tipo de borda do botão
    overrelief=RIDGE) # Efeito de relevo ao passar o mouse
 
b_1.place(x= 0, y= 0) # Posiciona o botão no frame_corpo


b_2 = Button(frame_corpo, command= lambda: entrar_valores('%'), text='%', width= 7, height=3, bg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x= 118, y= 0)

b_3 = Button(frame_corpo, command= lambda: entrar_valores('/'), text='/', width=7, height=3, bg=co4, fg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x= 178, y= 0)
b_4 = Button(frame_corpo, command= lambda: entrar_valores('*'),text='*', width= 7, height=3, bg=co4, fg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x= 178, y= 56)
b_5 = Button(frame_corpo, command= lambda: entrar_valores('-'),text='-', width=7, height=3, bg=co4, fg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x= 178, y= 112)
b_6 = Button(frame_corpo, command= lambda: entrar_valores('+'),text='+', width= 7, height=3, bg=co4, fg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x= 178, y= 168)
b_7 = Button(frame_corpo, command= calcular, text='=', width=7, height=3, bg=co4, fg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x= 178, y= 224)

b_8 = Button(frame_corpo, command= lambda: entrar_valores('0'),text='0', width= 16, height=3, bg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x= 0, y= 224)
b_9 = Button(frame_corpo, command= lambda: entrar_valores('.'),text='.', width= 7, height=3, bg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)

b_9.place(x= 118, y= 224)
b_10= Button(frame_corpo, command= lambda: entrar_valores('7'),text='7', width= 7, height=3, bg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x= 0, y= 56)
b_11= Button(frame_corpo, command= lambda: entrar_valores('8'),text='8', width= 7, height=3, bg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x= 59, y= 56)
b_11= Button(frame_corpo, command= lambda: entrar_valores('9'),text='9', width= 7, height=3, bg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)

b_11.place(x= 118, y= 56)
b_12= Button(frame_corpo, command= lambda: entrar_valores('6'),text='6', width= 7, height=3, bg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x= 0, y= 112)
b_13= Button(frame_corpo, command= lambda: entrar_valores('5'),text='5', width= 7, height=3, bg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x= 59, y= 112)
b_14= Button(frame_corpo, command= lambda: entrar_valores('4'),text='4', width= 7, height=3, bg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x= 118, y= 112)

b_15= Button(frame_corpo, command= lambda: entrar_valores('3'),text='3', width= 7, height=3, bg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x= 0, y= 168)
b_16= Button(frame_corpo, command= lambda: entrar_valores('2'),text='2', width= 7, height=3, bg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x= 59, y= 168)
b_17= Button(frame_corpo, command= lambda: entrar_valores('1'),text='1', width= 7, height=3, bg=co1 , font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x= 118, y= 168)




#chamando loop da janela para aparecer na tela e não fechar
janela.mainloop()