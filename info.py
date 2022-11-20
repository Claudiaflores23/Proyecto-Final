from cProfile import label
from os import stat
from util.generic import leer_imagen
from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("1355x580")
window.config(bg="white")
window.resizable(False,False)

plant_info = leer_imagen("recursos_img/info_back.png",(972,454))
barra_info = leer_imagen("recursos_img/barra_info.png",(582,45))
next1 = leer_imagen("recursos_img/next.png",(60,60))
privius = leer_imagen("recursos_img/previous.png",(60,60))
foto_grup1 = leer_imagen("images/grupoWf2.png",(375,281))
foto_grup2 = leer_imagen("images/grupo1.png",(375,281))
foto_grup3 = leer_imagen("images/plm-2v.png",(375,281))

lista_cuadros = [foto_grup1, foto_grup2, foto_grup3]
'''def cambio():
    frame_pr.destroy()'''
def adelante(num_imagen):
    global label_pre
    global btn_adelante
    global btn_atras

    label_pre.place_forget()
    label_pre = Label(frame1,image=lista_cuadros[num_imagen], bg="#1f5995")

    btn_atras = Button(frame_central,image=privius,bg="white",bd=0,activebackground="white", command=lambda: atras(num_imagen - 1))
    btn_adelante = Button(frame_central,image=next1, bg="white",bd=0,activebackground="white",command=lambda: adelante(num_imagen + 1))
    if num_imagen == 2:
        btn_adelante = Button(frame_central,image=next1, bg="white",bd=0,activebackground="white",state=DISABLED)

    label_pre.place(x=10,y=55)
    btn_atras.place(x=50,y=250)
    btn_adelante.place(x=1230,y=250)

def atras(num_imagen):
    global label_pre
    global btn_adelante
    global btn_atras

    label_pre.place_forget()
    label_pre = Label(frame1,image=lista_cuadros[num_imagen], bg="#1f5995")

    btn_atras = Button(frame_central,image=privius,bg="white",bd=0,activebackground="white", command=lambda: atras(num_imagen - 1))
    btn_adelante = Button(frame_central,image=next1, bg="white",bd=0,activebackground="white",command=lambda: adelante(num_imagen + 1))
    if num_imagen == 0:
        btn_atras = Button(frame_central,image=privius, bg="white",bd=0,activebackground="white",state=DISABLED)

    label_pre.place(x=10,y=55)
    btn_atras.place(x=50,y=250)
    btn_adelante.place(x=1230,y=250)


frame_central = Frame(window, height= 540, width=1355, bg="white")
frame_central.place(x=0,y=20)
back_labe = Label(frame_central, image=plant_info, height=454, width=972,bg="white")
back_labe.place(x=180, y=70)
barra_lab = Label(frame_central, image=barra_info,height=45, width=582,bg="white")
barra_lab.place(x=370,y=10)

btn_atras = Button(frame_central,image=privius,bg="white",bd=0,activebackground="white", state=DISABLED)
btn_atras.place(x=50,y=250)
btn_adelante = Button(frame_central,image=next1, bg="white",bd=0,activebackground="white",command=lambda: adelante(1))
btn_adelante.place(x=1230,y=250)

frame1 = Frame(frame_central, height=400, width=880, bg="#1f5995")
frame1.place(x=240,y=90)
label_pre = Label(frame1,image=foto_grup1, bg="#1f5995")
label_pre.place(x=10,y=55)



#frame_se = Frame(frame_central, height=400, width=400, bg="yellow")
#frame_se.place(x=710, y=90)
#Label(frame_se,text="Texto de prueba para comprobar el funcionamiento de este carrusel, este\n carrusel brindará información acerca de Plm y sus integrantes, hay que saber también\n que puede que este carrusel funcione o puede que no, así que debemos \nestar pendientes respecto a eso").place(x=1,y=55)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''estilo_paginas = ttk.Style()
estilo_paginas.configure("TNotebook",background ='white',foreground='white',padding=0,borderwidth=0)
estilo_paginas.theme_use('default')
estilo_paginas.configure("TNotebook",background='white',borderwidth=0)
estilo_paginas.configure("TNotebook.Tab",background='white',borderwidth=0)
estilo_paginas.map("TNotebook", background=[("selected",'white')])
estilo_paginas.map("TNotebook.Tab",background=[("selected",'white')],foreground=[("selected",'white')]);
notebook = ttk.Notebook(frame_central,style='TNotebook')
notebook.add(frame_pr)'''
window.mainloop()