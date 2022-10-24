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
    pavadinimas = e_pavadinimas.get()
    imones_kodas = int(e_imones_kodas.get())
    pvm_kodas = e_pvm_kodas.get()
    adresas = e_adresas.get()
    mokykla = Mokykla(pavadinimas=pavadinimas, imones_kodas=imones_kodas, pvm_kodas=pvm_kodas, adresas=adresas)
    session.add(mokykla)
    session.commit()
    l_mokykla_rezultatas["text"] = mokykla
    atnaujinti_mokyklos_laukus()

def mokyklu_listas():
    return session.query(Mokykla).all()

def atnaujinti_mokyklos_laukus():
    boxas.delete(0, END)
    boxas.insert(END, *mokyklu_listas())
    e_pavadinimas.delete(0, END)
    e_imones_kodas.delete(0, END)
    e_pvm_kodas.delete(0, END)
    e_adresas.delete(0, END)

def ivesti_studijas():
    programos_pavadinimas = e_programa.get()
    trukme = e_trukme.get()
    kaina = float(e_kaina.get())
    studijos = Studijos(programos_pavadinimas=programos_pavadinimas, trukme=trukme, kaina=kaina)
    session.add(studijos)
    session.commit()
    l_studijos_rezultatas["text"] = studijos
    atnaujinti_studijos_laukus()

def studiju_listas():
    return session.query(Studijos).all()

def atnaujinti_studijos_laukus():
    boxas.delete(0, END)
    boxas.insert(END, *studiju_listas())
    e_programa.delete(0, END)
    e_trukme.delete(0, END)
    e_kaina.delete(0, END)

def ivesti_studenta():
    vardas = e_vardas.get()
    pavarde = e_pavarde.get()
    asm_kodas = e_asmens_kodas.get()
    el_pastas = e_el_pastas.get()
    mobilus = e_mobilus.get()
    mokykla_id = pasirinkta_mokykla.get()
    studijos = pasirinktos_studijos.get()
    studijos_id = studijos.id
    studentas = Studentas(
        vardas=vardas, 
        pavarde=pavarde, 
        asm_kodas=asm_kodas, 
        el_pastas=el_pastas,
        mobilus=mobilus,
        mokykla_id=mokykla_id,
        studijos_id=studijos_id
    )
    session.add(studentas)
    session.commit()
    l_studentas_rezultatas["text"] = studentas
    atnaujinti_studento_laukus()

def studentu_listas():
    return session.query(Studentas).all()

def atnaujinti_studento_laukus():
    boxas.delete(0, END)
    boxas.insert(END, *studentu_listas())
    e_vardas.delete(0, END)
    e_pavarde.delete(0, END)
    e_asmens_kodas.delete(0, END)
    e_el_pastas.delete(0, END)
    e_mobilus.delete(0, END)

#cRud
def perziureti_mokyklas():
    boxas.delete(0, END)
    boxas.insert(END, *mokyklu_listas())

def perziureti_studijas():
    boxas.delete(0, END)
    boxas.insert(END, *studiju_listas())

def gauti_visus_studentus():
    studentu_sarasas = []
    studentai = session.query(Studentas).all()
    for studentas in studentai:
        studentu_sarasas.append(
            (studentas.vardas,
             studentas.pavarde,
              studentas.mokykla_id,
               studentas.studijos_id)
        )
    for studentas in studentu_sarasas:
        return studentas

def perziureti_studentus():
    boxas.delete(0, END)
    boxas.insert(END, *studentu_listas())
    tree.delete(*tree.get_children())
    tree.insert('', END, values=gauti_visus_studentus())

#crUd
def redaguoti_mokykla():
    pass

def redaguoti_studijas():
    pass

def redaguoti_studenta():
    pass

#cruD
def istrinti_mokykla():
    pazymeta_mokykla = boxas.curselection()[0]
    # mokykla = session.query(Mokykla).get(pazymeta_mokykla)
    # session.delete(mokykla)
    # session.commit()
    print(pazymeta_mokykla)

def istrinti_studijas():
    pazymetos_studijos = boxas.curselection()[0]
    studijos = session.query(Studijos).get(pazymetos_studijos)
    session.delete(studijos)
    session.commit()

def istrinti_studenta():
    pazymetas_studentas = boxas.curselection()[0]
    studentas = session.query(Studentas).get(pazymetas_studentas)
    session.delete(studentas)
    session.commit()

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
l_mokykla_rezultatas = Label(langas, text="", bd=2, relief=SUNKEN, bg='white')
l_tuscias_po_mokykla = Label(langas, text="")
l_ivesti_studijas = Label(langas, text="Įvesti studijų programą:")
l_programa = Label(langas, text="Programa")
l_trukme = Label(langas, text="Trukmė")
l_kaina = Label(langas, text="Kaina")
l_tuscias_pries_studijos = Label(langas, text="")
l_studijos_rezultatas = Label(langas, text="", bd=2, relief=SUNKEN, bg='white')
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
l_studentas_rezultatas = Label(langas, text="", bd=2, relief=SUNKEN, bg='white')
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

# combobox
mokyklos_pasirinkimas = session.query(Mokykla).all()
pasirinkta_mokykla = StringVar()
pasirinkta_mokykla.set(mokyklos_pasirinkimas[0])

mokyklos_comboboxas = ttk.Combobox(langas, values=mokyklos_pasirinkimas)
mokyklos_comboboxas.current(0)
mokyklos_comboboxas.bind("<<ComboboxSelected>>")
mokyklos_comboboxas.grid(row=22, column=2, ipadx=70)

studiju_pasirinkimas = session.query(Studijos).all()
pasirinktos_studijos = StringVar()
pasirinktos_studijos.set(studiju_pasirinkimas[0])

studiju_comboboxas = ttk.Combobox(langas, values=studiju_pasirinkimas)
studiju_comboboxas.current(0)
studiju_comboboxas.bind("<<ComboboxSelected>>")
studiju_comboboxas.grid(row=23, column=2, ipadx=70)

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
# e_mokykla.grid(row=22, column=2, ipadx=80)
# e_studijos.grid(row=23, column=2, ipadx=80)

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