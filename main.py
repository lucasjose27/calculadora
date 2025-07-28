#importando a biblioteca tkinter

from tkinter import *
from tkinter import ttk


#criando janela 

#cores
co1 = "#feffff"
co2 = "#38576b"  
co3 = "#BBBBBB"
co4 = '#FFAB40'

fundo = "#3b3b3b"

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x331')
janela.configure(bg=fundo)

#criando frames

frame_tela = Frame(janela, width=235, height= 50, bg=co2)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height= 280, bg=co1)
frame_corpo.grid(row=1, column=0)

todos_valores = ''

valor_texto = StringVar()

#criando função 

def entrar_valores(valor):
    
    global todos_valores
    todos_valores= todos_valores + str(valor) 
    
    #passando valor para tela 
    valor_texto.set(todos_valores)

#função para calculo

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(resultado)

#função limpar tela

def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

#criando label 
app_label= Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, bg=co2,fg=co1, font=('Ivy 18 '), anchor='e', justify=RIGHT)
app_label.place(x= 0, y=0) 



#criando os botões

b_1 = Button(frame_corpo, command=limpar_tela, text='C', width=16, height=3, bg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE) 
b_1.place(x= 0, y= 0)
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


janela.mainloop()   