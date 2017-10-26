# coding=utf-8
from Tkinter import *

class SolverWindow:
    def __init__(self, master):
        self.master = master
        self.conds = []

        master.title("Problemas de Programación Lineal")

        l = Label(master, text="Función objetivo")
        l.pack()

        self.w_z = Frame(master)

        l = Label(self.w_z, text="z=")
        l.pack(side=LEFT)

        self.txt_zc = []

        self.txt_zc.append(Entry(self.w_z,width=3,borderwidth=0,background=root["bg"],justify=RIGHT))
        self.txt_zc[0].insert(0,"0")
        self.txt_zc[0].pack(side=LEFT)
        l = Label(self.w_z, text="A +")
        l.pack(side=LEFT)

        self.txt_zc.append(Entry(self.w_z,width=3,borderwidth=0,background=root["bg"],justify=RIGHT))
        self.txt_zc[1].insert(0,"0")
        self.txt_zc[1].pack(side=LEFT)
        l = Label(self.w_z, text="B +")
        l.pack(side=LEFT)

        self.txt_zc.append(Entry(self.w_z,width=3,borderwidth=0,background=root["bg"],justify=RIGHT))
        self.txt_zc[2].insert(0,"0")
        self.txt_zc[2].pack(side=LEFT)
        l = Label(self.w_z, text="C +")
        l.pack(side=LEFT)

        self.txt_zc.append(Entry(self.w_z,width=3,borderwidth=0,background=root["bg"],justify=RIGHT))
        self.txt_zc[3].insert(0,"0")
        self.txt_zc[3].pack(side=LEFT)
        l = Label(self.w_z, text="D +")
        l.pack(side=LEFT)

        self.txt_zc.append(Entry(self.w_z,width=3,borderwidth=0,background=root["bg"],justify=RIGHT))
        self.txt_zc[4].insert(0,"0")
        self.txt_zc[4].pack(side=LEFT)
        l = Label(self.w_z, text="E")
        l.pack(side=LEFT)

        self.w_z.pack(padx=10)

        l = Label(master, text="s.a")
        l.pack()

        self.f_conds = Frame(master)

        self.f_conds.pack(padx=10)

        f_btns = Frame(master)

        self.btn_add = Button(f_btns, text="Agregar variable", command=self.add_variable)
        self.btn_add.pack(side=LEFT)

        self.btn_add = Button(f_btns, text="Agregar condición", command=self.add_condition)
        self.btn_add.pack(side=LEFT)

        self.btn_add = Button(f_btns, text="Resolver", command=self.greet)
        self.btn_add.pack(side=LEFT)

        f_btns.pack(anchor = "e",pady=10)

    def add_variable(self):
        self.txt_zc = []

        self.txt_zc.append(Entry(self.w_z, width=3, borderwidth=0, background=root["bg"], justify=RIGHT))
        self.txt_zc[0].insert(0, "0")
        self.txt_zc[0].pack(side=LEFT)
        l = Label(self.w_z, text="A +")
        l.pack(side=LEFT)

    def add_condition(self):
        f_cond = Frame(self.f_conds)

        coefs = []

        coefs.append(Entry(f_cond, width=3,borderwidth=0,background=root["bg"],justify=RIGHT))
        coefs[0].insert(0, "0")
        coefs[0].pack(side=LEFT)
        l = Label(f_cond, text="A +")
        l.pack(side=LEFT)

        coefs.append(Entry(f_cond, width=3,borderwidth=0,background=root["bg"],justify=RIGHT))
        coefs[1].insert(0, "0")
        coefs[1].pack(side=LEFT)
        l = Label(f_cond, text="B +")
        l.pack(side=LEFT)

        coefs.append(Entry(f_cond, width=3,borderwidth=0,background=root["bg"],justify=RIGHT))
        coefs[2].insert(0, "0")
        coefs[2].pack(side=LEFT)
        l = Label(f_cond, text="C +")
        l.pack(side=LEFT)

        coefs.append(Entry(f_cond, width=3,borderwidth=0,background=root["bg"],justify=RIGHT))
        coefs[3].insert(0, "0")
        coefs[3].pack(side=LEFT)
        l = Label(f_cond, text="D +")
        l.pack(side=LEFT)

        coefs.append(Entry(f_cond, width=3,borderwidth=0,background=root["bg"],justify=RIGHT))
        coefs[4].insert(0, "0")
        coefs[4].pack(side=LEFT)
        l = Label(f_cond, text="E =")
        l.pack(side=LEFT)

        coefs.append(Entry(f_cond, width=3,borderwidth=0,background=root["bg"],justify=RIGHT))
        coefs[5].insert(0, "0")
        coefs[5].pack(side=LEFT)

        f_cond.pack()

        f_cond.entries = coefs[:]
        self.conds.append(f_cond)


    def greet(self):
        print "lawl"
root = Tk()
my_gui = SolverWindow(root)
root.mainloop()