from email.mime import image
from tkinter import *
from tkinter.font import BOLD
import pymysql
from tkinter import messagebox
import mariadb
import util.generic as utl

class master_register:    
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('Sign Up')
        self.ventana.geometry('400x500')
        self.ventana.config(bg='white')
        self.ventana.iconbitmap("images/iconi.ico")
        self.ventana.resizable(width=0,height=0)
        utl.centrar_ventana(self.ventana,400,500)

        self.logo_plm = utl.leer_imagen("images/plm_logo.png", (245,140))

        frame_logo = Frame(self.ventana, width=300, height=200, bg="white").place(x=50, y=10)
        label = Label(self.ventana, image=self.logo_plm, bg='white').place(x=75, y=20)

        frame = Frame(self.ventana, width=300, height=300, bg="white")
        frame.place(x=50, y=170)

        heading = Label(frame, text="Sign up", fg="#FCBA40", bg="white", font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=83, y=20)

        self.user_entry = Entry(frame, width=30, fg='black', border = 0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.user_entry.place(x=40, y=85)
        def on_enter(e):
            self.user_entry.delete(0, 'end')

        def on_leave(e):
            name =self.user_entry.get()
            if name =="":
                self.user_entry.insert(0,'Username')
        self.user_entry.insert(0, 'Username')
        self.user_entry.bind("<FocusIn>", on_enter)
        self.user_entry.bind("<FocusOut>", on_leave)
        Frame(frame, width=250, height=2, bg='#FCBA40').place(x=15, y=107)
        
        def on_enter(e):
            self.pass_entry.delete(0, 'end')
            self.pass_entry.config(show="*")

        def on_leave(e):
            name = self.pass_entry.get()
            if name == "":
                self.pass_entry.config(show="")
                self.pass_entry.insert(0,'Password')

        self.pass_entry = Entry(frame, width=30, fg='black', border=0, bg="white",font=('Microsoft YaHei UI Light', 11))
        self.pass_entry.place(x=40, y=140)
        self.pass_entry.insert(0, 'Password')
        self.pass_entry.bind("<FocusIn>", on_enter)
        self.pass_entry.bind("<FocusOut>", on_leave)
        Frame(frame, width=250, height=2, bg='#FCBA40').place(x=15, y=162)

        def on_enter(e):
            pass_entry_two.delete(0, 'end')
            pass_entry_two.config(show="*")

        def on_leave(e):
            name =pass_entry_two.get()
            if name == "":
                pass_entry_two.config(show="")
                pass_entry_two.insert(0,'Rewrite password')

        pass_entry_two = Entry(frame, width=30, fg='black', border=0, bg="white",font=('Microsoft YaHei UI Light', 11))
        pass_entry_two.place(x=40, y=200)
        pass_entry_two.insert(0, 'Rewrite password')
        pass_entry_two.bind("<FocusIn>", on_enter)
        pass_entry_two.bind("<FocusOut>", on_leave)
        Frame(frame, width=250, height=2, bg='#FCBA40').place(x=16, y=222)

        self.userico = utl.leer_imagen("images/userco.png",(15,15))
        label_user=Label(frame, image=self.userico, bg='white').place(x=15, y=85)

        self.passico = utl.leer_imagen("images/cerrar-con-llave.png",(15,15))
        label_passico=Label(frame,image=self.passico, bg='white').place(x=15, y=140)
        label_passico_2=Label(frame,image=self.passico, bg='white').place(x=15, y=200)

        def show():
            hide_button = Button(frame, image=hide_photo, bg='white', activebackground='white', cursor='hand2', bd=0, command=hide)
            hide_button.place(x=245, y=144)
            self.pass_entry.config(show='')
        def hide():
            show_button = Button(frame, image=photo, bg='white', activebackground='white', cursor='hand2', bd=0, command=show)
            show_button.place(x=245, y=144)
            self.pass_entry.config(show='*')
        photo= utl.leer_imagen('images/show.png', (16,16))
        #photo = ImageTk.PhotoImage(show_image)
        show_button = Button(frame, image=photo, bg='white', activebackground='white', cursor='hand2', bd=0, command=show)
        show_button.place(x=245, y=144)
        hide_photo= utl.leer_imagen('images/esconder.png', (16,16))

        Button(frame, width=30, pady=7, text='Sign up', bg="#035596", activebackground="#CFF7FF", cursor= 'hand2', fg='white', border=0, command=self.inserta_datos).place(x=35, y=250)

    def consulta_est(self, query):
        try:
            conn = mariadb.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "bd",
                autocommit = True
            )
        except mariadb.Error as e:
            print("Error al conectarse a la base de datos", e)
        cur = conn.cursor()
        cur.execute(query)
        return cur

    def inserta_datos(self):
        if len(self.user_entry.get())!=0 and len(self.pass_entry.get())!=0:
            query ="INSERT INTO `login` (`id`, `user`, `password`) VALUES (NULL, '"+self.user_entry.get()+"', '"+self.pass_entry.get()+"');" 
            self.consulta_est(query)
            self.mensaje['text']="El estudiante "+self.user_entry.get()+" se ha insertado exitosamente"
            self.user_entry.delete(0, END)
            self.pass_entry.delete(0, END)
            self.user_entry.focus()
        else:
            self.mensaje['text']="El nombre y el password del estudiante no pueden estar vacíos"

        self.ventana.mainloop()