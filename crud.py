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

pasirinktas_id = IntVar()

#Crud
def ivesti_mokykla():
    pavadinimas = e_pavadinimas.get()
    imones_kodas = int(e_imones_kodas.get())
    pvm_kodas = e_pvm_kodas.get()
    adresas = e_adresas.get()
    mokykla = Mokykla(
        pavadinimas=pavadinimas, 
        imones_kodas=imones_kodas, 
        pvm_kodas=pvm_kodas, 
        adresas=adresas
    )
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
    mokykla_id = e_mokykla_id.get()
    studijos = Studijos(
        programos_pavadinimas=programos_pavadinimas, 
        trukme=trukme, 
        kaina=kaina, 
        mokykla_id=mokykla_id
    )
    session.add(studijos)
    session.commit()
    # l_studijos_rezultatas["text"] = studijos
    atnaujinti_studijos_laukus()

def ikelti_mokykla_studijoms():
    pazymeta_mokykla = session.query(Mokykla).all()[boxas.curselection()[0]]
    pasirinktas_id.set(pazymeta_mokykla.id)
    reikalinga_mokykla = session.query(Mokykla).get(pazymeta_mokykla.id)
    e_mokykla_id.insert(0, reikalinga_mokykla.id)
    
def studiju_listas():
    return session.query(Studijos).all()

def atnaujinti_studijos_laukus():
    boxas.delete(0, END)
    boxas.insert(END, *studiju_listas())
    e_programa.delete(0, END)
    e_trukme.delete(0, END)
    e_kaina.delete(0, END)
    e_mokykla_id.delete(0, END)

def ivesti_studenta():
    vardas = e_vardas.get()
    pavarde = e_pavarde.get()
    asm_kodas = e_asmens_kodas.get()
    el_pastas = e_el_pastas.get()
    mobilus = e_mobilus.get()
    studijos_id = e_studijos.get()
    studentas = Studentas(
        vardas=vardas, 
        pavarde=pavarde, 
        asm_kodas=asm_kodas, 
        el_pastas=el_pastas,
        mobilus=mobilus,
        studijos_id=studijos_id
    )
    session.add(studentas)
    session.commit()
    # l_studentas_rezultatas["text"] = studentas
    atnaujinti_studento_laukus()

def ikelti_studijas_studentui():
    pazymeta_studijos = session.query(Studijos).all()[boxas.curselection()[0]]
    pasirinktas_id.set(pazymeta_studijos.id)
    reikalinga_studijos = session.query(Studijos).get(pazymeta_studijos.id)
    e_studijos.insert(0, reikalinga_studijos.id)

def studentu_listas():
    return session.query(Studentas).all()

def atnaujinti_studento_laukus():
    boxas.delete(0, END)
    boxas.insert(END, *studentu_listas())
    tree.delete(*tree.get_children())
    studentu_sarasas = []
    studentai = session.query(Studentas).all()
    for studentas in studentai:
        studentu_sarasas.append(
            (studentas.vardas,
            studentas.pavarde,
            studentas.studijos_id)
        )
    for studentas in studentu_sarasas:
        tree.insert('', END, values=studentas)
    e_vardas.delete(0, END)
    e_pavarde.delete(0, END)
    e_asmens_kodas.delete(0, END)
    e_el_pastas.delete(0, END)
    e_mobilus.delete(0, END)
    e_studijos.delete(0, END)

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
            studentas.studijos_id)
        )
    for studentas in studentu_sarasas:
        return studentas

def perziureti_studentus():
    boxas.delete(0, END)
    boxas.insert(END, *studentu_listas())
    tree.delete(*tree.get_children())
    studentu_sarasas = []
    studentai = session.query(Studentas).all()
    for studentas in studentai:
        studentu_sarasas.append(
            (studentas.vardas,
            studentas.pavarde,
            studentas.studijos_id)
        )
    for studentas in studentu_sarasas:
        tree.insert('', END, values=studentas)
#crUd
def ikelti_mokykla():
    pazymeta_mokykla = session.query(Mokykla).all()[boxas.curselection()[0]]
    pasirinktas_id.set(pazymeta_mokykla.id)
    redaguojama_mokykla = session.query(Mokykla).get(pazymeta_mokykla.id)
    atnaujinti_mokyklos_laukus()
    e_pavadinimas.insert(0, redaguojama_mokykla.pavadinimas)
    e_imones_kodas.insert(0, redaguojama_mokykla.imones_kodas)
    e_pvm_kodas.insert(0, redaguojama_mokykla.pvm_kodas)
    e_adresas.insert(0, redaguojama_mokykla.adresas)
    b_redaguoti_mokykla["state"] = ACTIVE

def redaguoti_mokykla():
    pasirinkta_mokykla = pasirinktas_id.get()
    redaguojama_mokykla = session.query(Mokykla).get(pasirinkta_mokykla) 
    redaguojama_mokykla.pavadinimas = e_pavadinimas.get()
    redaguojama_mokykla.imones_kodas = e_imones_kodas.get()
    redaguojama_mokykla.pvm_kodas = e_pvm_kodas.get()
    redaguojama_mokykla.adresas = e_adresas.get()
    session.commit()
    l_mokykla_rezultatas["text"] = f"{redaguojama_mokykla.pavadinimas} atnaujinta"
    atnaujinti_mokyklos_laukus()
    b_redaguoti_mokykla['state'] = DISABLED

def ikelti_studijas():
    pazymeta_studijos = session.query(Studijos).all()[boxas.curselection()[0]]
    pasirinktas_id.set(pazymeta_studijos.id)
    redaguojama_studijos = session.query(Studijos).get(pazymeta_studijos.id)
    atnaujinti_studijos_laukus()
    e_programa.insert(0, redaguojama_studijos.programos_pavadinimas)
    e_trukme.insert(0, redaguojama_studijos.trukme)
    e_kaina.insert(0, redaguojama_studijos.kaina)
    e_mokykla_id.insert(0, redaguojama_studijos.mokykla_id)
    b_redaguoti_studijas["state"] = ACTIVE

def redaguoti_studijas():
    pasirinkta_studijos = pasirinktas_id.get()
    redaguojama_studijos = session.query(Studijos).get(pasirinkta_studijos) 
    redaguojama_studijos.programos_pavadinimas = e_programa.get()
    redaguojama_studijos.trukme = e_trukme.get()
    redaguojama_studijos.kaina = e_kaina.get()
    redaguojama_studijos.mokykla_id = e_mokykla_id.get()
    session.commit()
    l_studijos_rezultatas["text"] = f"{redaguojama_studijos.programos_pavadinimas} atnaujinta"
    atnaujinti_studijos_laukus()
    b_redaguoti_studijas['state'] = DISABLED

def ikelti_studenta():
    pazymetas_studentas = session.query(Studentas).all()[boxas.curselection()[0]]
    pasirinktas_id.set(pazymetas_studentas.id)
    redaguojamas_studentas = session.query(Studentas).get(pazymetas_studentas.id)
    atnaujinti_studento_laukus()
    e_vardas.insert(0, redaguojamas_studentas.vardas)
    e_pavarde.insert(0, redaguojamas_studentas.pavarde)
    e_asmens_kodas.insert(0, redaguojamas_studentas.asm_kodas)
    e_el_pastas.insert(0, redaguojamas_studentas.el_pastas)
    e_mobilus.insert(0, redaguojamas_studentas.mobilus)
    e_studijos.insert(0, redaguojamas_studentas.studijos_id)
    b_redaguoti_studenta["state"] = ACTIVE

def redaguoti_studenta():
    pasirinktas_studentas = pasirinktas_id.get()
    redaguojamas_studentas = session.query(Studentas).get(pasirinktas_studentas) 
    redaguojamas_studentas.vardas = e_vardas.get()
    redaguojamas_studentas.pavarde = e_pavarde.get()
    redaguojamas_studentas.asm_kodas = e_asmens_kodas.get()
    redaguojamas_studentas.el_pastas = e_el_pastas.get()
    redaguojamas_studentas.mobilus = e_mobilus.get()
    redaguojamas_studentas.studijos_id = e_studijos.get()
    session.commit()
    l_studentas_rezultatas["text"] = f"{redaguojamas_studentas.vardas} atnaujinta"
    atnaujinti_studento_laukus()
    b_redaguoti_studenta['state'] = DISABLED

#cruD
def istrinti_mokykla():
    pazymeta_mokykla = mokyklu_listas()[boxas.curselection()[0]]
    mokykla = session.query(Mokykla).get(pazymeta_mokykla.id)
    session.delete(mokykla)
    session.commit()
    boxas.delete(0, END)
    boxas.insert(END, *mokyklu_listas())
    l_mokykla_rezultatas["text"] = f"{pazymeta_mokykla.pavadinimas} ištrinta"

def istrinti_studijas():
    pazymetos_studijos = studiju_listas()[boxas.curselection()[0]]
    studijos = session.query(Studijos).get(pazymetos_studijos.id)
    session.delete(studijos)
    session.commit()
    boxas.delete(0, END)
    boxas.insert(END, *studiju_listas())
    l_studijos_rezultatas["text"] = f"{pazymetos_studijos.programos_pavadinimas} ištrinta"

def istrinti_studenta():
    pazymetas_studentas = studentu_listas()[boxas.curselection()[0]]
    studentas = session.query(Studentas).get(pazymetas_studentas.id)
    session.delete(studentas)
    session.commit()
    boxas.delete(0, END)
    boxas.insert(END, *studentu_listas())
    l_studentas_rezultatas["text"] = f"{pazymetas_studentas.vardas} {pazymetas_studentas.pavarde} ištrintas"

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
l_mokykla_id = Label(langas, text="Mokymo įstaiga")
l_tuscias_pries_studijos = Label(langas, text="")
l_studijos_rezultatas = Label(langas, text="", bd=2, relief=SUNKEN, bg='white')
l_tuscias_po_studijos = Label(langas, text="")
l_ivesti_studenta = Label(langas, text="Įvesti studentą:")
l_vardas = Label(langas, text="Vardas")
l_pavarde = Label(langas, text="Pavardė")
l_asmens_kodas = Label(langas, text="Asmens kodas")
l_el_pastas = Label(langas, text="El. paštas")
l_mobilus = Label(langas, text="Mobilus tel. nr.")
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
e_mokykla_id = Entry(langas)
e_vardas = Entry(langas)
e_pavarde = Entry(langas)
e_asmens_kodas = Entry(langas)
e_el_pastas = Entry(langas)
e_mobilus = Entry(langas)
e_studijos = Entry(langas)

# Buttons
b_ivesti_mokykla = Button(langas, text="Įrašyti", command=ivesti_mokykla)
b_ikelti_mokykla = Button(langas, text="Įkelti", command=ikelti_mokykla)
b_redaguoti_mokykla = Button(langas, text="Redaguoti", command=redaguoti_mokykla, state=DISABLED)
b_istrinti_mokykla = Button(langas, text="Ištrinti", command=istrinti_mokykla)
b_ivesti_studijas = Button(langas, text="Įrašyti", command=ivesti_studijas)
b_ikelti_studijas = Button(langas, text="Įkelti redagavimui", command=ikelti_studijas)
b_redaguoti_studijas = Button(langas, text="Redaguoti", command=redaguoti_studijas, state=DISABLED)
b_istrinti_studijas = Button(langas, text="Ištrinti", command=istrinti_studijas)
b_ivesti_studenta = Button(langas, text="Įrašyti", command=ivesti_studenta)
b_ikelti_studenta = Button(langas, text="Įkelti redagavimui", command=ikelti_studenta)
b_redaguoti_studenta = Button(langas, text="Redaguoti", command=redaguoti_studenta, state=DISABLED)
b_istrinti_studenta = Button(langas, text="Ištrinti", command=istrinti_studenta)
b_pasirinkti_mokykla = Button(langas, text="įkelti mokyklą", command=ikelti_mokykla_studijoms)
b_pasirinkti_studijas = Button(langas, text="įkelti studijas", command=ikelti_studijas_studentui)

# listbox
boxo_scrollbaras = Scrollbar(langas)
boxas = Listbox(langas, yscrollcommand=boxo_scrollbaras.set, height=20, width=130, selectmode=SINGLE)
boxo_scrollbaras.config(command=boxas.yview)
boxas.grid(row=1, rowspan=15, column=6, sticky=W+E)
boxo_scrollbaras.grid(row=1, rowspan=15, column=7, sticky=N+S)
b_rodyti_mokyklas = Button(langas, text="Rodyti mokymo įstaigas", command=perziureti_mokyklas)
b_rodyti_studijas = Button(langas, text="Rodyti studijų programas", command=perziureti_studijas)
b_rodyti_studentus = Button(langas, text="Rodyti studentus", command=perziureti_studentus)
b_rodyti_mokyklas.grid(row=6, column=9, sticky=W+E)
b_rodyti_studijas.grid(row=8, column=9, sticky=W+E)
b_rodyti_studentus.grid(row=10, column=9, sticky=W+E)

# treeview students
columns = ('vardas', 'pavarde', 'studijos')
tree = ttk.Treeview(langas, columns=columns, show='headings', height=10)

tree.column('vardas', width=150)
tree.column('pavarde', width=150)
tree.column('studijos', width=150)

tree.heading('vardas', text="Vardas")
tree.heading('pavarde', text="Pavardė")
tree.heading('studijos', text="Studijų programos ID")

studentu_sarasas = []
studentai = session.query(Studentas).all()
for studentas in studentai:
    studentu_sarasas.append(
        (studentas.vardas,
        studentas.pavarde,
        studentas.studijos_id)
    )
for studentas in studentu_sarasas:
    tree.insert('', END, values=studentas)

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
l_mokykla_id.grid(row=13, column=1, sticky=W)
l_tuscias_pries_studijos.grid(row=14, column=1, sticky=W)
l_studijos_rezultatas.grid(row=15, column=1, columnspan=4, sticky=W+E)
l_tuscias_po_studijos.grid(row=16, column=1, sticky=W)
l_ivesti_studenta.grid(row=17, column=1, sticky=W)
l_vardas.grid(row=18, column=1, sticky=W)
l_pavarde.grid(row=19, column=1, sticky=W)
l_asmens_kodas.grid(row=20, column=1, sticky=W)
l_el_pastas.grid(row=21, column=1, sticky=W)
l_mobilus.grid(row=22, column=1, sticky=W)
l_studijos.grid(row=23, column=1, sticky=W)
l_tuscias_pries_studentas.grid(row=25, column=1, sticky=W)
l_studentas_rezultatas.grid(row=26, column=1, columnspan=4, sticky=W+E)
l_tuscias_po_studentas.grid(row=27, column=1, sticky=W)

# grids for entries
e_pavadinimas.grid(row=2, column=2, ipadx=80)
e_imones_kodas.grid(row=3, column=2, ipadx=80)
e_pvm_kodas.grid(row=4, column=2, ipadx=80)
e_adresas.grid(row=5, column=2, ipadx=80)
e_programa.grid(row=10, column=2, ipadx=80)
e_trukme.grid(row=11, column=2, ipadx=80)
e_kaina.grid(row=12, column=2, ipadx=80)
e_mokykla_id.grid(row=13, column=2, ipadx=80)
e_vardas.grid(row=18, column=2, ipadx=80)
e_pavarde.grid(row=19, column=2, ipadx=80)
e_asmens_kodas.grid(row=20, column=2, ipadx=80)
e_el_pastas.grid(row=21, column=2, ipadx=80)
e_mobilus.grid(row=22, column=2, ipadx=80)
e_studijos.grid(row=23, column=2, ipadx=80)

# grids for buttons
b_ivesti_mokykla.grid(row=2, column=4, sticky=W+E)
b_ikelti_mokykla.grid(row=3, column=4, sticky=W+E)
b_redaguoti_mokykla.grid(row=4, column=4, sticky=W+E)
b_istrinti_mokykla.grid(row=5, column=4, sticky=W+E)
b_ivesti_studijas.grid(row=10, column=4, sticky=W+E)
b_ikelti_studijas.grid(row=11, column=4, sticky=W+E)
b_redaguoti_studijas.grid(row=12, column=4, sticky=W+E)
b_istrinti_studijas.grid(row=13, column=4, sticky=W+E)
b_pasirinkti_mokykla.grid(row=14, column=4, sticky=W+E)
b_ivesti_studenta.grid(row=18, column=4, sticky=W+E)
b_ikelti_studenta.grid(row=19, column=4, sticky=W+E)
b_redaguoti_studenta.grid(row=20, column=4, sticky=W+E)
b_istrinti_studenta.grid(row=21, column=4, sticky=W+E)
b_pasirinkti_studijas.grid(row=22, column=4, sticky=W+E)

langas.mainloop()