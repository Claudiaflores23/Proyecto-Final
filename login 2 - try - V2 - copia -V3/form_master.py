try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

from doctest import master
from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from setuptools import Command
from util.generic import leer_imagen

class Fullscreen_Example(tk.Tk):
    def __init__(self,*args,**kwargs):
        #super().__init__(*args,**kwargs)
        self.window = tk.Tk()
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

        self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (self.w, self.h))
        self.window.config(bg='white')
        self.window.iconbitmap("images/iconi.ico")
        
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)
        self.frame_principal = Frame(self.window, bg='white')
        self.frame_principal.grid(column=1, row=1, sticky='nsew')
        self.frame_principal.columnconfigure(1,weight=1)
        self.frame_principal.rowconfigure(1,weight=1)
        self.frame_principal.place(x=1, y=105)
        self.widgets()


    def testone(self):
        self.notebook.select([self.page2])
        self.page2.columnconfigure(0, weight=1)
		#self.page2.columnconfigure(1, weight=1)
		#self.page2.rowconfigure(2, weight=1)
    def home(self):
        self.notebook.select([self.page1])
        self.page1.columnconfigure(0, weight=1)
    def stadistics(self):
        self.notebook.select([self.page3])
        self.page3.columnconfigure(0, weight=1)
    def info_f(self):
        self.notebook.select([self.page4])
        self.page4.columnconfigure(0, weight=1)
    '''def stadistics1(self):
        self.page1.destroy()
        self.page2.destroy()
        self.page3.place(x=5,y=130)'''


    def widgets(self):
        self.submit1 = leer_imagen("recursos_img/submit1.png",(105,80))
        self.submit2 = leer_imagen("recursos_img/submit2.png",(105,80))
        self.frame_en = leer_imagen("recursos_img/frame_entry.png",(900,80))
        self.frame_en2 = leer_imagen("recursos_img/frame_entry2.png",(900,400))
        self.plant_info = leer_imagen("recursos_img/info_back.png",(972,454))
        self.barra_info = leer_imagen("recursos_img/barra_info.png",(582,45))
        self.next1 = leer_imagen("recursos_img/next.png",(60,60))
        self.privius = leer_imagen("recursos_img/previous.png",(60,60))
        self.foto_grup1 = leer_imagen("images/grupoWf2.png",(375,281))
        self.foto_grup2 = leer_imagen("images/grupo1.png",(375,281))
        self.foto_grup3 = leer_imagen("images/plm-2v.png",(375,281))


        estilo_paginas = ttk.Style()
        estilo_paginas.configure("TNotebook",background ='white',foreground='white',padding=0,borderwidth=0)
        estilo_paginas.theme_use('default')
        estilo_paginas.configure("TNotebook",background='white',borderwidth=0)
        estilo_paginas.configure("TNotebook.Tab",background='white',borderwidth=0)
        estilo_paginas.map("TNotebook", background=[("selected",'white')])
        estilo_paginas.map("TNotebook.Tab",background=[("selected",'white')],foreground=[("selected",'white')]);
        
        self.notebook = ttk.Notebook(self.frame_principal,style='TNotebook')
        self.notebook.grid(column=0,row=0,sticky='nsew')
        self.page1= Frame(self.window,width=1355,height=580,bg="white")
        self.page2= Frame(self.window,width=1355,height=580,bg="white")
        self.page3= Frame(self.window,width=1355,height=580,bg="white")
        self.page4= Frame(self.window,width=1355,height=580,bg="white")
        self.notebook.add(self.page1)
        self.notebook.add(self.page2)
        self.notebook.add(self.page3)
        self.notebook.add(self.page4)

####################################################PAGE ONE#################################################################################################

        self.navbar = leer_imagen("recursos_img/barranv.png",(1260,100))
        self.info = leer_imagen("recursos_img/info_con.png",(80,80))
        self.stadistic = leer_imagen("recursos_img/stadistic_con.png",(80,80))
        frame_opbar=Frame(self.page1, width=1325, height=200, bg="white").place(x=20, y=10)
        label = Label(frame_opbar, image=self.navbar, bg='white').place(x=50, y=20)
        info = Button(frame_opbar, image=self.info, bg = "#FCBA40",bd=0, activebackground="#FCBA40",command=self.info_f).place(x=340,y= 30)
        stadistic = Button(frame_opbar, image=self.stadistic, bg="#FCBA40",bd=0,activebackground="#FCBA40",command=self.stadistics).place(x=970,y=30)
#--------------------botones------------------------------------------------------------------------
        imagen1 = leer_imagen("recursos_img/pg1.png",(200,200))
        imagen2 = leer_imagen("recursos_img/pg2.png",(200,200))
        def enter(e):
            bt_op1["image"] =imagen2
            bt_op1.image=imagen2
        def leave(e):
            bt_op1["image"] =imagen1
            bt_op1.image=imagen1
        frame_seg1=Frame(self.page1,width=250,height=250,bg="white")
        frame_seg1.place(x=95,y=135)
        bt_op1=Button(frame_seg1,image=imagen1,bg="white",bd=0, command=self.testone)
        bt_op1.bind("<Enter>",enter)
        bt_op1.bind("<Leave>",leave)
        bt_op1.place(x=20,y=20)
#------boton 2------
        imagen3 = leer_imagen("recursos_img/lo1.png",(200,200))
        imagen4 = leer_imagen("recursos_img/lo2.png",(200,200))
        def enter1(e):
            bt_op2["image"] =imagen4
            bt_op2.image=imagen4
        def leave1(e):
            bt_op2["image"] =imagen3
            bt_op2.image=imagen3
        frame_seg2=Frame(self.page1,width=250,height=250,bg="white")
        frame_seg2.place(x=395,y=135)
        bt_op2=Button(frame_seg2,image=imagen3,bg="white",bd=0)
        bt_op2.bind("<Enter>",enter1)
        bt_op2.bind("<Leave>",leave1)
        bt_op2.place(x=20,y=20)
#-------boton 3-------
        imagen5 = leer_imagen("recursos_img/ps1.png",(200,200))
        imagen6 = leer_imagen("recursos_img/ps2.png",(200,200))
        def enter2(e):
            bt_op3["image"] =imagen6
            bt_op3.image=imagen6
        def leave2(e):
            bt_op3["image"] =imagen5
            bt_op3.image=imagen5
        frame_seg3=Frame(self.page1,width=250,height=250,bg="white")
        frame_seg3.place(x=695,y=135)
        bt_op3=Button(frame_seg3,image=imagen5,bg="white",bd=0)
        bt_op3.bind("<Enter>",enter2)
        bt_op3.bind("<Leave>",leave2)
        bt_op3.place(x=20,y=20)
#--------boton 4--------
        imagen7 = leer_imagen("recursos_img/lm1.png",(200,200))
        imagen8 = leer_imagen("recursos_img/lm2.png",(200,200))
        def enter3(e):
            bt_op4["image"] =imagen8
            bt_op4.image=imagen8
        def leave3(e):
            bt_op4["image"] =imagen7
            bt_op4.image=imagen7
        frame_seg4=Frame(self.page1,width=250,height=250,bg="white")
        frame_seg4.place(x=995,y=135)
        bt_op4=Button(frame_seg4,image=imagen7,bg="white",bd=0)
        bt_op4.bind("<Enter>",enter3)
        bt_op4.bind("<Leave>",leave3)
        bt_op4.place(x=20,y=20)
#-----------------burger menu----------
        sidebar=leer_imagen("recursos_img/sidebar.png",(190,700))
        menuburger=leer_imagen("recursos_img/burgermenu.png",(40,40))
        menuburger2=leer_imagen("recursos_img/burgermenu2.png",(40,40))
        userico=leer_imagen("recursos_img/useric.png",(35,35))
        exitbt = leer_imagen("recursos_img/exitbt.png",(28,28))

        def toggle_win():
            f1=Frame(self.window,width=190,height=760,bg="white")
            f1.place(x=1170,y=13)
            Label(f1, image=sidebar,bg="white").place(x=0,y=0)

            def dele():
                f1.destroy()


            Button(f1,image=menuburger2,command=dele,border=0,activebackground='#035596',bg='#035596').place(x=35,y=34)
            Button(f1,image=userico,bg="#035596",bd=0,activebackground="#035596",command=self.home).place(x=35,y=90)
            Button(f1,image=exitbt,bg="#035596",bd=0,activebackground="#035596",command=self.window.destroy).place(x=130,y=640)
            Frame(f1, width=178, height=2, bg='white').place(x=7, y=198)
            pg_bt = Button(f1,text="Coding",width=17,height=1,bg="#035596",fg='white',bd=0,activebackground="#035596",activeforeground="light blue",command=self.testone)
            pg_bt.config(font =("Helvetica",14))
            pg_bt.place(x=5,y=200)
            Frame(f1, width=178, height=2, bg='white').place(x=7, y=234)
            pg_bt1 = Button(f1,text="Logic",width=17,height=1,bg="#035596",fg='white',bd=0,activebackground="#035596",activeforeground="light blue")
            pg_bt1.config(font =("Helvetica",14))
            pg_bt1.place(x=5,y=236)
            Frame(f1, width=178, height=2, bg='white').place(x=7, y=270)
            pg_bt2 = Button(f1,text="PsInt",width=17,height=1,bg="#035596",fg='white',bd=0,activebackground="#035596",activeforeground="light blue")
            pg_bt2.config(font =("Helvetica",14))
            pg_bt2.place(x=5,y=272)
            Frame(f1, width=178, height=2, bg='white').place(x=7, y=306)
            pg_bt2 = Button(f1,text="Math logic",width=17,height=1,bg="#035596",fg='white',bd=0,activebackground="#035596",activeforeground="light blue")
            pg_bt2.config(font =("Helvetica",14))
            pg_bt2.place(x=5,y=308)
            Frame(f1, width=178, height=2, bg='white').place(x=7, y=342)
            
        burgerbtn =Button(frame_opbar,image=menuburger,bg="#FCBA40",bd=0,activebackground="#FCBA40",command=toggle_win)
        burgerbtn.place(x=1200,y=52)

###############################################################PAGE TWO################################################################################################################
        #Label(self.page2,text="Hola mundo").place(x=1,y=1)
        progress_frame1 = Frame(self.page2, width=1325, height=70,bg ="white")
        progress_frame1.place(x=10,y=20)

        #ans_entry = Frame(self.page2, height=80,width=900,bg="white").place(x=250,y=450)
        frame_text= Frame(self.page2,bd=0,width=990,height=100,padx=0,bg="white")
        frame_text.place(x=200,y=205)
        Label(frame_text,text="Este es un texto de ejemplo para poder probar y calcular el tamaño que tendran los textos\n en este segmento, me gustaria que dentro del codigo esto en lugar de ampliarse se dividiera\n en parrafo.",
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=5,y=5)
        frame_text1= Frame(self.page2,bd=0,width=1020,height=100,padx=0,bg="white")
        Label(frame_text1,text="Segundo texto de prueba que verdaderamente siento que no va a funcionar puesto que todo las\nlongitudes de un texto son distintas unas de otras, pero bueno que se le va a hacer a toda\nesta situación",
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=5,y=5)
        t = ttk.Style()
        t.theme_use('default')
        t.configure(
            "custom.Horizontal.TProgressbar",
            troughcolor='white',
            background='#FCBA40',
            darkcolor="light blue",
            bordercolor="#FCBA40"
        )
        progress_in = ttk.Progressbar(progress_frame1,style="custom.Horizontal.TProgressbar",orient="horizontal",length=1260,mode='determinate')
        progress_in.place(x=45,y=20)
        self.ans = []
        def obtener_respuesta():
            self.ans.append(ans_en.get())          
            print(self.ans)


        def aumento():
            obtener_respuesta()
            ans_en.delete(0, 'end')
            progress_in['value']+=20
            frame_text.destroy()
            frame_text1.place(x=170,y=205)

        def enter(e):
            submit_bt["image"] =self.submit2
            submit_bt.image=self.submit2
        def leave(e):
            submit_bt["image"] =self.submit1
            submit_bt.image=self.submit1
        submit_bt=Button(self.page2, image=self.submit1,bg="white",bd=0,activebackground="white",command=aumento)
        submit_bt.bind("<Enter>",enter)
        submit_bt.bind("<Leave>",leave)
        submit_bt.place(x=1000,y=490)

        ans_entry = Frame(self.page2, height=80,width=900,bg="white")
        ans_entry.place(x=250,y=370)
        entrt_fr = Label(ans_entry,image=self.frame_en,bg="white")
        entrt_fr.place(x=1,y=2)
        def on_enter(e):
            ans_en.delete(0, 'end')

        def on_leave(e):
            name =ans_en.get()
            if name =="":
                ans_en.insert(0,'Type here...')
        ans_en = Entry(ans_entry, width=77, fg='black', border = 0, bg="white", font=('Microsoft YaHei UI Light', 15))
        ans_en.place(x=27,y=30)
        ans_en.insert(0,'Type here...') 
        ans_en.bind("<FocusIn>", on_enter)  
        ans_en.bind("<FocusOut>", on_leave)
        
################################################################PAGE THREE###############################################################
        nombres = ['Programación','Lógica matemática','PSint','Lógica']
        colores = ['#035596','#FCBA40','#035596','#FCBA40']
        tamaño = [15,25,10,30]
        fig, axs = plt.subplots(dpi=80, figsize=(8,6), sharey=True, facecolor='white')
        plt.title('Graphic per category',color='#035596',size=16,family="Arial")

        axs.bar(nombres,tamaño,color=colores)
        #axs[1].plot(nombres,tamaño,color="orange")
        
        canvas = FigureCanvasTkAgg(fig,master=self.page3)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0,row=0,rowspan=3)
###############################################################PAGE FOUR###############################################################
        lista_cuadros = [self.foto_grup1, self.foto_grup2, self.foto_grup3]
        def adelante(num_imagen):
            global label_pre
            global btn_adelante
            global btn_atras

            self.label_pre.place_forget()
            self.label_pre = Label(frame1,image=lista_cuadros[num_imagen], bg="#1f5995")

            btn_atras = Button(frame_central,image=self.privius,bg="white",bd=0,activebackground="white", command=lambda: atras(num_imagen - 1))
            btn_adelante = Button(frame_central,image=self.next1, bg="white",bd=0,activebackground="white",command=lambda: adelante(num_imagen + 1))
            if num_imagen == 2:
                btn_adelante = Button(frame_central,image=self.next1, bg="white",bd=0,activebackground="white",state=DISABLED)

            self.label_pre.place(x=10,y=55)
            btn_atras.place(x=50,y=250)
            btn_adelante.place(x=1230,y=250)

        def atras(num_imagen):
            global label_pre
            global btn_adelante
            global btn_atras

            self.label_pre.place_forget()
            self.label_pre = Label(frame1,image=lista_cuadros[num_imagen], bg="#1f5995")

            btn_atras = Button(frame_central,image=self.privius,bg="white",bd=0,activebackground="white", command=lambda: atras(num_imagen - 1))
            btn_adelante = Button(frame_central,image=self.next1, bg="white",bd=0,activebackground="white",command=lambda: adelante(num_imagen + 1))
            if num_imagen == 0:
                btn_atras = Button(frame_central,image=self.privius, bg="white",bd=0,activebackground="white",state=DISABLED)

            self.label_pre.place(x=10,y=55)
            btn_atras.place(x=50,y=250)
            btn_adelante.place(x=1230,y=250)


        frame_central = Frame(self.page4, height= 540, width=1355, bg="white")
        frame_central.place(x=1,y=20)
        back_labe = Label(frame_central, image=self.plant_info, height=454, width=972,bg="white")
        back_labe.place(x=180, y=70)
        barra_lab = Label(frame_central, image=self.barra_info,height=45, width=582,bg="white")
        barra_lab.place(x=370,y=10)

        btn_atras = Button(frame_central,image=self.privius,bg="white",bd=0,activebackground="white", state=DISABLED)
        btn_atras.place(x=50,y=250)
        btn_adelante = Button(frame_central,image=self.next1, bg="white",bd=0,activebackground="white",command=lambda: adelante(1))
        btn_adelante.place(x=1230,y=250)

        frame1 = Frame(frame_central, height=400, width=880, bg="#1f5995")
        frame1.place(x=240,y=90)
        self.label_pre = Label(frame1,image=self.foto_grup1, bg="#1f5995")
        self.label_pre.place(x=10,y=55)
        #self.page1.place(x=5,y=130)
        #self.page2.place(x=5,y=130)
        #self.page3.place(x=5,y=130)
        self.notebook.pack(padx=5,pady=5)
        self.window.mainloop()




    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)
    
    
        
'''if __name__ == '__main__':
    app = Fullscreen_Example()'''
