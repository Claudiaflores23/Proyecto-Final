from tkinter import *
from tkinter import Tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from util.generic import leer_imagen

class stadistic():
    def __init__(self):
        self.st_window = Tk()
        self.fullScreenState = False
        self.st_window.attributes("-fullscreen", self.fullScreenState)

        self.w, self.h = self.st_window.winfo_screenwidth(), self.st_window.winfo_screenheight()
        self.st_window.geometry("%dx%d" % (self.w, self.h))
        self.st_window.config(bg='white')
        self.st_window.iconbitmap("images/iconi.ico")
        
        self.st_window.bind("<F11>", self.toggleFullScreen)
        self.st_window.bind("<Escape>", self.quitFullScreen)
        #self.grafic = Frame(self.st_window, height=300, width=500, bg='white').place(x=200,y=295)
        frame_opbar=Frame(self.st_window, width=1325, height=200, bg="white").place(x=20, y=10)
        frame_graficbar = Frame(self.st_window, bg="white")
        frame_graficbar.grid(column=0,row=0,sticky='nsew')
        frame_graficbar.place(x=700, y=170)

        nombres = ['Programación','Lógica matemática','PSint','Lógica']
        colores = ['#035596','#FCBA40','#035596','#FCBA40']
        tamaño = [15,25,10,30]
        fig, axs = plt.subplots(1,2,dpi=80, figsize=(8,6), sharey=True, facecolor='white')
        plt.title('Graphic per category',color='#035596',size=16,family="Arial")

        axs[0].bar(nombres,tamaño,color=colores)
        axs[1].plot(nombres,tamaño,color="orange")
        
        canvas = FigureCanvasTkAgg(fig,master=frame_graficbar)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0,row=0,rowspan=3)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
        fig, ax = plt.subplots(dpi=90,figsize=(7,5),facecolor='white')
        plt.title("Avarage graphic", color='#035596',size=16,family="Arial")

        plt.xlim(-4,14)
        plt.ylim(-8,8)
        ax.set_facecolor('white')

        ax.axhline(linewidth=2,color='r')
        ax.axvline(linewidth=2,color='r')

        ax.set_xlabel("Eje horizontal",color='black')
        ax.set_ylabel("Eje vertical",color='black')
        ax.tick_params(direction='out',length=6,width=2,
            colors='black',
            grid_color='r',
            grid_alpha=0.5)
        
        def graficar_datos():
            #nivel=scale.get()
            nivel = 8
            x = np.arange(-np.pi, 4*np.pi,0.01)
            if nivel <= 4:
                line, = ax.plot(x, nivel*np.sin(x),color='red',linestyle="solid")
            else:
                if nivel <= 7:
                    line, = ax.plot(x, nivel*np.sin(x),color='orange',linestyle="solid")
                else:
                    line, = ax.plot(x, nivel*np.sin(x),color='green',linestyle="solid")

            canvas.draw()

            #self.label.config(text=nivel)
            line.set_ydata(np.sin(x)+10)

            self.st_window.after(100, graficar_datos)
        frame = Frame(self.st_window, bg='white',bd=3)
        frame.grid(column=0, row=0)
        frame.place(x=50, y=170)

        canvas=FigureCanvasTkAgg(fig,master=frame)
        canvas.get_tk_widget().grid(column=0,row=0,columnspan=3,padx=5,pady=5)

        Button(frame, text='Graphic it!', width=15, bg='#035596',fg='white',bd=0, command=graficar_datos).grid(column=0,row=1,pady=5)
        #self.label= Label(frame,width=15)
        #self.label.grid(column=1,row=1,pady=5)

        #scale=ttk.Scale(frame, to=6,from_=0,orient='horizontal',length=300)
        #scale.grid(column=2, row=1)

        style = ttk.Style()
        style.configure("Horizontal.TScale", background='gray22')
#----------------------------------------------------------------------------------------------------------------------------------------------------
        self.navbar = leer_imagen("recursos_img/barranv.png",(1260,100))
        self.info = leer_imagen("recursos_img/info_con.png",(80,80))
        self.stadistic = leer_imagen("recursos_img/stadistic_con.png",(80,80))
        label = Label(frame_opbar, image=self.navbar, bg='white').place(x=50, y=20)
        info = Button(frame_opbar, image=self.info, bg = "#FCBA40",   bd=0, activebackground="#FCBA40").place(x=340,y= 30)
        stadistic = Button(frame_opbar, image=self.stadistic, bg="#FCBA40",bd=0,activebackground="#FCBA40").place(x=970,y=30)

        sidebar=leer_imagen("recursos_img/sidebar.png",(190,700))
        menuburger=leer_imagen("recursos_img/burgermenu.png",(40,40))
        menuburger2=leer_imagen("recursos_img/burgermenu2.png",(40,40))
        userico=leer_imagen("recursos_img/useric.png",(35,35))
        exitbt = leer_imagen("recursos_img/exitbt.png",(28,28))

        def toggle_win():
            f1=Frame(self.st_window,width=190,height=760,bg="white")
            f1.place(x=1170,y=13)
            Label(f1, image=sidebar,bg="white").place(x=0,y=0)

            def dele():
                f1.destroy()


            Button(f1,image=menuburger2,command=dele,border=0,activebackground='#035596',bg='#035596').place(x=35,y=34)
            Button(f1,image=userico,bg="#035596",bd=0,activebackground="#035596").place(x=35,y=90)
            Button(f1,image=exitbt,bg="#035596",bd=0,activebackground="#035596",command=self.st_window.destroy).place(x=130,y=640)
            Frame(f1, width=178, height=2, bg='white').place(x=7, y=198)
            pg_bt = Button(f1,text="Coding",width=17,height=1,bg="#035596",fg='white',bd=0,activebackground="#035596",activeforeground="light blue")
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





        self.st_window = mainloop()
    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)
        
if __name__ == '__main__':
    app = stadistic() 