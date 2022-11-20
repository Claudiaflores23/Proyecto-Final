from tkinter import *
import tkinter as tk
from tkinter import ttk
import time
import util.generic as utl
from form_master import Fullscreen_Example

class load:
    def __init__(self):
        root=Tk()
        root.title("Loading...")
        root.geometry('925x500')
        root.config(bg="white")
        root.iconbitmap("images/iconi.ico")
        utl.centrar_ventana(root,925,500)

        logo = utl.leer_imagen("images/plm_logo.png",(305,170))
        Label(root, image=logo, bg='white').place(x=315, y=150)


        def step():
            #myprogres['value']+=20
            for x in range(100):
                myprogres['value']+=1
                root.update_idletasks()
                time.sleep(0.05)
                label.config(text=myprogres['value'])
            if myprogres['value'] == 100:
                root.destroy()
                Fullscreen_Example()
            #myprogres.start(10)

        progresframe=Frame(root,width=300,height=100,bg="white")
        progresframe.place(x=325,y=350)
        s = ttk.Style()
        s.theme_use('clam')

        s.configure(
            "custom.Horizontal.TProgressbar",
            troughcolor='white',
            background='#FCBA40',
            darkcolor="gray",
            lightcolor="light blue",
            bordercolor="black",
            )
        myprogres =ttk.Progressbar(progresframe,style= "custom.Horizontal.TProgressbar",orient="horizontal",length=300,mode='determinate')
        myprogres.pack(pady=20)

        labelframe=Frame(root,width=80,height=80,bg="white")
        labelframe.place(x=470,y=400)

        label=Label(root,text="",pady=20,bg="white",fg="white")
        label.place(x=470,y=410)
        step()
        root.mainloop()
