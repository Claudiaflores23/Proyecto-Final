from os import name
from tkinter import *
import tkinter as tk
from tkinter import ttk
from util.generic import leer_imagen

class test(tk.Tk):
    def __init__(self):
        self.testy = tk.Tk()
        self.fullScreenState = False
        self.testy.attributes("-fullscreen", self.fullScreenState)
        self.w, self.h = self.testy.winfo_screenwidth(), self.testy.winfo_screenheight()
        self.testy.geometry("%dx%d" % (self.w, self.h))
        self.testy.config(bg='white')
        self.testy.iconbitmap("images/iconi.ico")
        
        self.testy.bind("<F11>", self.toggleFullScreen)
        self.testy.bind("<Escape>", self.quitFullScreen)
        
        self.submit1 = leer_imagen("recursos_img/submit1.png",(105,80))
        self.submit2 = leer_imagen("recursos_img/submit2.png",(105,80))
        self.next = leer_imagen("recursos_img/next.png",(60,60))
        self.privius = leer_imagen("recursos_img/previous.png",(60,60))
        self.navbar = leer_imagen("recursos_img/barranv.png",(1260,100))
        self.info = leer_imagen("recursos_img/info_con.png",(80,80))
        self.stadistic = leer_imagen("recursos_img/stadistic_con.png",(80,80))
        self.frame_en = leer_imagen("recursos_img/frame_entry.png",(900,80))
        self.frame_en2 = leer_imagen("recursos_img/frame_entry2.png",(900,400))
        sidebar=leer_imagen("recursos_img/sidebar.png",(190,700))
        menuburger=leer_imagen("recursos_img/burgermenu.png",(40,40))
        menuburger2=leer_imagen("recursos_img/burgermenu2.png",(40,40))
        userico=leer_imagen("recursos_img/useric.png",(35,35))
        exitbt = leer_imagen("recursos_img/exitbt.png",(28,28))
        frame_opbar=Frame(self.testy, width=1325, height=200, bg="white").place(x=20, y=10)
        label = Label(frame_opbar, image=self.navbar, bg='white').place(x=50, y=20)
        info = Button(frame_opbar, image=self.info, bg = "#FCBA40",   bd=0, activebackground="#FCBA40").place(x=340,y= 30)
        stadistic = Button(frame_opbar, image=self.stadistic, bg="#FCBA40",bd=0,activebackground="#FCBA40").place(x=970,y=30)
        
        ans_entry = Frame(self.testy, height=80,width=900,bg="red").place(x=250,y=450)
        frame_text= Frame(self.testy,bd=0,width=990,height=100,padx=0,bg="white")
        frame_text.place(x=200,y=295)
        Label(frame_text,text="Este es un texto de ejemplo para poder probar y calcular el tamaño que tendran los textos\n en este segmento, me gustaria que dentro del codigo esto en lugar de ampliarse se dividiera\n en parrafo.",
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=5,y=5)
        frame_text1= Frame(self.testy,bd=0,width=990,height=100,padx=0,bg="white")
        Label(frame_text1,text="Segundo texto de prueba que verdaderamente siento que no va a funcionar puesto que todo las\nlongitudes de un texto son distintas unas de otras, pero bueno que se le va a hacer a toda\nesta situación",
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=5,y=5)

        progress_frame1 = Frame(self.testy, width=1325, height=70,bg ="white").place(x=20,y=170)
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
        progress_in.place(x=50,y=180)
        def obtener_respuesta():
            ans = []
            ans.insert(-1,ans_en.get())

            
            print(ans)


        def aumento():
            obtener_respuesta()
            ans_en.delete(0, 'end')
            progress_in['value']+=20
            frame_text.destroy()
            frame_text1.place(x=200,y=295)
            
            
        def enter(e):
            submit_bt["image"] =self.submit2
            submit_bt.image=self.submit2
        def leave(e):
            submit_bt["image"] =self.submit1
            submit_bt.image=self.submit1
        submit_bt=Button(self.testy, image=self.submit1,bg="white",bd=0,activebackground="white",command=aumento)
        submit_bt.bind("<Enter>",enter)
        submit_bt.bind("<Leave>",leave)
        submit_bt.place(x=1050,y=550)
#-----------------------------------------------------------------------------------------------------------------------
        ans_entry = Frame(self.testy, height=80,width=900,bg="white").place(x=250,y=450)
        entrt_fr = Label(ans_entry,image=self.frame_en,bg="white").place(x=250,y=450)
        def on_enter(e):
            ans_en.delete(0, 'end')

        def on_leave(e):
            name =ans_en.get()
            if name =="":
                ans_en.insert(0,'Type here...')
        ans_en = Entry(ans_entry, width=77, fg='black', border = 0, bg="white", font=('Microsoft YaHei UI Light', 15))
        ans_en.place(x=276,y=478)
        ans_en.insert(0,'Type here...') 
        ans_en.bind("<FocusIn>", on_enter)  
        ans_en.bind("<FocusOut>", on_leave)
        def toggle_win():
            f1=Frame(self.testy,width=190,height=760,bg="white")
            f1.place(x=1170,y=13)
            Label(f1, image=sidebar,bg="white").place(x=0,y=0)

            def dele():
                f1.destroy()


            Button(f1,image=menuburger2,command=dele,border=0,activebackground='#035596',bg='#035596').place(x=35,y=34)
            Button(f1,image=userico,bg="#035596",bd=0,activebackground="#035596").place(x=35,y=90)
            Button(f1,image=exitbt,bg="#035596",bd=0,activebackground="#035596",command=self.testy.destroy).place(x=130,y=640)
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
#-----------------------------------------------------------------------------------------------------------------------
        '''def on_enter(e):
            ans_en1.delete(0, 'end')

        def on_leave(e):
            name =ans_en.get()
            if name =="":
                ans_en1.insert(0,'Type here...')
        ans_en1 = Entry(ans_entry, width=77, fg='black', border = 0, bg="white", font=('Microsoft YaHei UI Light', 15))
        ans_en1.insert(0,'Type here...') 
        ans_en1.bind("<FocusIn>", on_enter)  
        ans_en1.bind("<FocusOut>", on_leave)'''
        #Button(progress_frame1,height=5,width=20,bg="red",command=aumento).place(x=300,y=400)


        self.testy.mainloop()




        

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.testy.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.testy.attributes("-fullscreen", self.fullScreenState)


if __name__ == '__main__':
    appT = test() 
