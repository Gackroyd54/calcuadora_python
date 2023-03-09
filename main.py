from tkinter import *
from tkinter import ttk
cor1 = "#3b3b3b" #preto
cor2="#feffff" #branco
cor3="#38573b" #Azul
cor4="#ECEFF1" #cinza
cor5 ="#FFAB40" #laranja
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")

#Criando a função para inserir os caracteres
def calcular():
    resultado = eval("9/9")
    valor_texto.set(resultado)
    
    
    
    
    
valor_texto = StringVar()

#Criando os frames(Repartições da janela principal)
frame_janela = Frame(janela,width=240,height = 50,bg=cor3)
janela.config(bg=cor1)
frame_janela.grid(row=0,column=0)
frame_corpo = Frame(janela,width=240,height=268)
frame_corpo.grid(row = 1,column = 0)

#Colocando o visor
app_label = Label(frame_janela,textvariable= valor_texto,width=16,height =2,padx = 7,relief =FLAT,anchor ='e',justify=RIGHT,font =('Ivy 14'),bg = cor3)
app_label.place(x = 0,y = 0)

#Criando os botões:
b1 = Button(frame_corpo,text = "C",width =9 ,height =2 ,bg = cor4,overrelief=RIDGE)
#b1.place(x = 0,y = 0)
b1.place(x = 0,y = 0)
b2 = Button(frame_corpo,text = "%",width = 6,height = 2,bg = cor4,overrelief=RIDGE)
b2.place(x = 108,y = 0)
b3 = Button(frame_corpo,text = "/",width = 4,height = 2,bg = cor5,fg = cor2,overrelief=RIDGE )
b3.place(x = 177, y = 0)
b4 = Button(frame_corpo,text = "7",width=4,height =2,bg = cor4,overrelief = RIDGE)
b4.place(x = 0,y = 49)
b5 = Button(frame_corpo,text = '8',width = 4,height = 2,bg = cor4,overrelief=RIDGE)
b5.place(x = 63,y=49)
b6 = Button(frame_corpo,text = "9",width = 3,height = 2,bg = cor4,overrelief = RIDGE)
b6.place(x =125,y = 49)
b7 = Button(frame_corpo,text = "*",width = 4,height = 2,bg = cor5,overrelief=RIDGE)
b7.place(x=177,y=49)
b8 = Button(frame_corpo,text = '6',width = 4,height = 2,bg = cor4,overrelief = RIDGE)
b8.place(x = 0,y=98)
b9 = Button(frame_corpo,text = '5',width = 4,height = 2,bg = cor4,overrelief=RIDGE)
b9.place(x = 63,y = 98)
b10= Button(frame_corpo,text = '4', width = 3, height = 2,bg = cor4,overrelief=RIDGE)
b10.place(x = 125,y =98)
b11 = Button(frame_corpo,text = '-',width = 4,height = 2,bg = cor5,overrelief=RIDGE)
b11.place(x = 177,y = 98)
b12 = Button(frame_corpo,text = "1",width = 4,height = 2,bg = cor4,overrelief = RIDGE)
b12.place(x=0,y = 147)
b13 =Button(frame_corpo, text = "2",width = 4,height = 2,bg = cor4,overrelief=RIDGE)
b13.place(x = 63,y = 147)
b14 = Button(frame_corpo,text = "3",width = 3,height = 2,bg = cor4,overrelief =RIDGE )
b14.place(x = 125,y = 147)
b15 = Button(frame_corpo,text = "+",width = 4,height = 2,bg = cor5,overrelief=RIDGE)
b15.place(x = 177,y = 147)
b16 = Button(frame_corpo,text = "0",width = 17,height = 2,bg = cor4,overrelief=RIDGE)
b16.place(x=0,y = 196)
b17 = Button(frame_corpo,text ="=",width = 4,height = 2,bg = cor5,overrelief = RIDGE)
b17.place(x = 177,y =196 )


calcular()
#comando para executar
janela.mainloop()
