# coding=utf-8
from Tkinter import *
from ttk import Combobox
from Equation import Equation
from LinearProblem import LinearProblem
from AnalyticSolver import AnalyticSolver
from RandomSolver import RandomSolver
import numpy as np

class SolverWindow:
    def __init__(self, master):
        self.master = master
        self.vars = []
        self.conds = []
        self.l = None

        master.title("Problemas de Programación Lineal")

        l = Label(master, text="Función objetivo")
        l.pack()

        self.w_z = Frame(master)

        self.ptype = Combobox(self.w_z,width=3)
        self.ptype['values'] = ('Min','Max')
        self.ptype.set('Max')
        self.ptype.pack(side=LEFT)

        l = Label(self.w_z, text="z=")
        l.pack(side=LEFT)

        self.w_z.pack(padx=10)

        l = Label(master, text="s.a")
        l.pack()

        self.f_conds = Frame(master)

        self.f_conds.pack(padx=10)

        f_btns = Frame(master)

        self.btn_add = Button(f_btns, text="Agregar\nvariable", command=self.add_variable)
        self.btn_add.pack(side=LEFT)

        self.btn_add = Button(f_btns, text="Agregar\ncondición", command=self.add_condition)
        self.btn_add.pack(side=LEFT)

        self.btn_add = Button(f_btns, text="Resolver\nAnalítico", command=self.solve_analytic)
        self.btn_add.pack(side=LEFT)

        self.btn_add = Button(f_btns, text="Resolver\nAleatorios", command=self.solve_random)
        self.btn_add.pack(side=LEFT)

        f_btns.pack(anchor = "e",pady=10,padx=10)

        self.lbl_ans = Label(master, justify=CENTER)
        self.lbl_ans.pack()

    def add_variable(self):

        e = Entry(self.w_z, width=3, borderwidth=0, background=root["bg"], justify=RIGHT)

        self.vars.append(e)

        e.insert(0, "0")
        e.pack(side=LEFT)

        c = ord('A')+len(self.vars)-1

        if self.l is not None:
            self.l['text'] = str(chr(c-1))+" +"

        self.l = Label(self.w_z, text=str(chr(c)))
        self.l.pack(side=LEFT)

    def add_condition(self):
        f_cond = Frame(self.f_conds)

        coefs = []

        ch = ord('A')

        for i in range(len(self.vars)):
            c = Entry(f_cond, width=3,borderwidth=0,background=root["bg"],justify=RIGHT)
            c.insert(0, "0")
            c.pack(side=LEFT)

            coefs.append(c)

            txt = str(chr(ch))

            if i < len(self.vars)-1:
                txt = txt+ " +"
            l = Label(f_cond, text=txt)
            ch = ch+1
            l.pack(side=LEFT)

        type = Combobox(f_cond,width=3,justify=CENTER)
        type['values'] = ('<','<=','=','>=','>')
        type.set('<=')
        type.pack(side=LEFT)

        v = Entry(f_cond, width=3, borderwidth=0, background=root["bg"], justify=RIGHT)
        v.insert(0, "0")
        v.pack(side=LEFT)

        f_cond.pack()

        f_cond.coefs = coefs[:]
        f_cond.type = type
        f_cond.value = v
        self.conds.append(f_cond)

    def getlinearproblem(self):
        coefs = [np.float(c.get()) for c in self.vars]

        z = Equation(coefs)

        conds = [Equation(
            [np.float(t.get()) for t in c.coefs],
            c.type.current() + 1,
            np.float(c.value.get())
        ) for c in self.conds]

        p = LinearProblem(z, conds, self.ptype.current())
        return p

    def solve_analytic(self):
        self.solve(AnalyticSolver)

    def solve_random(self):
        self.solve(RandomSolver)

    def solve(self,solver):
        p = self.getlinearproblem()

        ch = ord('A')

        point,z = solver.solve(p)

        txt = ""

        for i in range(len(self.vars)):
            txt = txt+str(point[i])+chr(ch+i)
            if i<len(self.vars)-1:
                txt = txt+" + "
            else:
                txt = txt+" = "
        txt = txt+str(z)

        self.lbl_ans['text'] = txt

root = Tk()
my_gui = SolverWindow(root)
root.mainloop()