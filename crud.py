from tkinter import *
from tkinter import ttk
from sqlalchemy.orm import sessionmaker
from model import engine, Mokykla, Studijos, Studentas

langas = Tk()
langas.geometry("1600x650")
langas.title("Persikvalifikuojančių į IT sritį asmenų duomenų bazė v1.0")
ikonele = PhotoImage(file="image/student.png")
langas.iconphoto(True, ikonele)

session = sessionmaker(bind=engine)()

#Crud
def ivesti_mokykla():
    pass

def ivesti_studijas():
    pass

def ivesti_studenta():
    pass

def atnaujinti_laukus():
    pass

#cRud
def perziureti_mokyklas():
    pass

def perziureti_studijas():
    pass

def perziureti_studentus():
    pass

#crUd

def redaguoti_mokykla():
    pass

def redaguoti_studijas():
    pass

def redaguoti_studenta():
    pass

#cruD

def istrinti_mokykla():
    pass

def istrinti_studijas():
    pass

def istrinti_studenta():
    pass

# Labels
l_tuscias_e0_s0 = Label(langas, text="")
l_tuscias_e0_s3 = Label(langas, text="")
l_tuscias_e0_s5 = Label(langas, text="")
l_tuscias_e0_s8 = Label(langas, text="")
l_ivesti_mokykla = Label(langas, text="Įvesti mokymo įstaigą:")
l_pavadinimas = Label(langas, text="Pavadinimas")
l_imones_kodas = Label(langas, text="Įmonės kodas")
l_pvm_kodas = Label(langas, text="PVM kodas")
l_adresas = Label(langas, text="Adresas")
l_tuscias_pries_mokykla = Label(langas, text="")
l_mokykla_rezultatas = Label(langas, text="", bd=2, relief=SUNKEN, anchor=W, bg='white')
l_tuscias_po_mokykla = Label(langas, text="")
l_ivesti_studijas = Label(langas, text="Įvesti studijų programą:")
l_programa = Label(langas, text="Programa")
l_trukme = Label(langas, text="Trukmė")
l_kaina = Label(langas, text="Kaina")
l_tuscias_pries_studijos = Label(langas, text="")
l_studijos_rezultatas = Label(langas, text="", bd=2, relief=SUNKEN, anchor=W, bg='white')
l_tuscias_po_studijos = Label(langas, text="")
l_ivesti_studenta = Label(langas, text="Įvesti studentą:")
l_vardas = Label(langas, text="Vardas")
l_pavarde = Label(langas, text="Pavardė")
l_asmens_kodas = Label(langas, text="Asmens kodas")
l_el_pastas = Label(langas, text="El. paštas")
l_mobilus = Label(langas, text="Mobilus tel. nr.")
l_mokykla = Label(langas, text="Mokymo įstaiga")
l_studijos = Label(langas, text="Studijos")
l_tuscias_pries_studentas = Label(langas, text="")
l_studentas_rezultatas = Label(langas, text="", bd=2, relief=SUNKEN, anchor=W, bg='white')
l_tuscias_po_studentas = Label(langas, text="")

# Entries
e_pavadinimas = Entry(langas)
e_imones_kodas = Entry(langas)
e_pvm_kodas = Entry(langas)
e_adresas = Entry(langas)
e_programa = Entry(langas)
e_trukme = Entry(langas)
e_kaina = Entry(langas)
e_vardas = Entry(langas)
e_pavarde = Entry(langas)
e_asmens_kodas = Entry(langas)
e_el_pastas = Entry(langas)
e_mobilus = Entry(langas)
e_mokykla = Entry(langas)
e_studijos = Entry(langas)

# Buttons
b_ivesti_mokykla = Button(langas, text="Įrašyti", command=ivesti_mokykla)
b_redaguoti_mokykla = Button(langas, text="Redaguoti", command=redaguoti_mokykla)
b_istrinti_mokykla = Button(langas, text="Ištrinti", command=istrinti_mokykla)
b_ivesti_studijas = Button(langas, text="Įrašyti", command=ivesti_studijas)
b_redaguoti_studijas = Button(langas, text="Redaguoti", command=redaguoti_studijas)
b_istrinti_studijas = Button(langas, text="Ištrinti", command=istrinti_studijas)
b_ivesti_studenta = Button(langas, text="Įrašyti", command=ivesti_studenta)
b_redaguoti_studenta = Button(langas, text="Redaguoti", command=redaguoti_studenta)
b_istrinti_studenta = Button(langas, text="Ištrinti", command=istrinti_studenta)

# listbox
boxo_scrollbaras = Scrollbar(langas)
boxas = Listbox(langas, yscrollcommand=boxo_scrollbaras.set, height=20, width=150, selectmode=SINGLE)
boxo_scrollbaras.config(command=boxas.yview)
boxas.grid(row=1, rowspan=15, column=6, sticky=W+E)
boxo_scrollbaras.grid(row=1, rowspan=15, column=7, sticky=N+S)
b_rodyti_mokyklas = Button(langas, text="Rodyti mokymo įstaigas", command=perziureti_mokyklas)
b_rodyti_studijas = Button(langas, text="Rodyti studijų programas", command=perziureti_studijas)
b_rodyti_studentus = Button(langas, text="Rodyti studentus", command=perziureti_studentus)
b_rodyti_mokyklas.grid(row=6, column=9, sticky=W+E)
b_rodyti_studijas.grid(row=8, column=9, sticky=W+E)
b_rodyti_studentus.grid(row=10, column=9, sticky=W+E)

# treeview
columns = ('vardas', 'pavarde', 'pavadinimas', 'programos_pavadinimas')
tree = ttk.Treeview(langas, columns=columns, show='headings', height=10)

tree.column('vardas', width=150)
tree.column('pavarde', width=150)
tree.column('pavadinimas', width=200)
tree.column('programos_pavadinimas', width=250)

tree.heading('vardas', text="Vardas")
tree.heading('pavarde', text="Pavardė")
tree.heading('pavadinimas', text="Mokymo įstaiga")
tree.heading('programos_pavadinimas', text="Studijų programa")

tree.grid(row=16, rowspan=25, column=6, sticky=W+E)
tree_scrollbaras = ttk.Scrollbar(langas, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=tree_scrollbaras.set)
tree_scrollbaras.grid(row=16, rowspan=25, column=7, sticky=N+S)

# grids for labels
l_tuscias_e0_s0.grid(row=0, column=0)
l_tuscias_e0_s3.grid(row=0, column=3)
l_tuscias_e0_s5.grid(row=0, column=5)
l_tuscias_e0_s8.grid(row=0, column=8)
l_ivesti_mokykla.grid(row=1, column=1, sticky=W)
l_pavadinimas.grid(row=2, column=1, sticky=W)
l_imones_kodas.grid(row=3, column=1, sticky=W)
l_pvm_kodas.grid(row=4, column=1, sticky=W)
l_adresas.grid(row=5, column=1, sticky=W)
l_tuscias_pries_mokykla.grid(row=6, column=1, sticky=W)
l_mokykla_rezultatas.grid(row=7, column=1, columnspan=4, sticky=W+E)
l_tuscias_po_mokykla.grid(row=8, column=1, sticky=W)
l_ivesti_studijas.grid(row=9, column=1, sticky=W)
l_programa.grid(row=10, column=1, sticky=W)
l_trukme.grid(row=11, column=1, sticky=W)
l_kaina.grid(row=12, column=1, sticky=W)
l_tuscias_pries_studijos.grid(row=13, column=1, sticky=W)
l_studijos_rezultatas.grid(row=14, column=1, columnspan=4, sticky=W+E)
l_tuscias_po_studijos.grid(row=15, column=1, sticky=W)
l_ivesti_studenta.grid(row=16, column=1, sticky=W)
l_vardas.grid(row=17, column=1, sticky=W)
l_pavarde.grid(row=18, column=1, sticky=W)
l_asmens_kodas.grid(row=19, column=1, sticky=W)
l_el_pastas.grid(row=20, column=1, sticky=W)
l_mobilus.grid(row=21, column=1, sticky=W)
l_mokykla.grid(row=22, column=1, sticky=W)
l_studijos.grid(row=23, column=1, sticky=W)
l_tuscias_pries_studentas.grid(row=24, column=1, sticky=W)
l_studentas_rezultatas.grid(row=25, column=1, columnspan=4, sticky=W+E)
l_tuscias_po_studentas.grid(row=26, column=1, sticky=W)

# grids for entries
e_pavadinimas.grid(row=2, column=2, ipadx=80)
e_imones_kodas.grid(row=3, column=2, ipadx=80)
e_pvm_kodas.grid(row=4, column=2, ipadx=80)
e_adresas.grid(row=5, column=2, ipadx=80)
e_programa.grid(row=10, column=2, ipadx=80)
e_trukme.grid(row=11, column=2, ipadx=80)
e_kaina.grid(row=12, column=2, ipadx=80)
e_vardas.grid(row=17, column=2, ipadx=80)
e_pavarde.grid(row=18, column=2, ipadx=80)
e_asmens_kodas.grid(row=19, column=2, ipadx=80)
e_el_pastas.grid(row=20, column=2, ipadx=80)
e_mobilus.grid(row=21, column=2, ipadx=80)
e_mokykla.grid(row=22, column=2, ipadx=80)
e_studijos.grid(row=23, column=2, ipadx=80)

# grids for buttons
b_ivesti_mokykla.grid(row=2, column=4, sticky=W+E)
b_redaguoti_mokykla.grid(row=3, column=4, sticky=W+E)
b_istrinti_mokykla.grid(row=4, column=4, sticky=W+E)
b_ivesti_studijas.grid(row=10, column=4, sticky=W+E)
b_redaguoti_studijas.grid(row=11, column=4, sticky=W+E)
b_istrinti_studijas.grid(row=12, column=4, sticky=W+E)
b_ivesti_studenta.grid(row=19, column=4, sticky=W+E)
b_redaguoti_studenta.grid(row=20, column=4, sticky=W+E)
b_istrinti_studenta.grid(row=21, column=4, sticky=W+E)

langas.mainloop()