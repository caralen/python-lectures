"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Graficko sucelje
NASLOV              Tkinter GUI modulom
                    Password Generator
"""
import random
import tkinter as tk


root = tk.Tk()
root.title("Algebra - Python programer")
# root.geometry("600x400")

# GLOBALNE VARIJABLE
slova_var = tk.BooleanVar()
brojevi_var = tk.BooleanVar()
spec_znakovi_var = tk.BooleanVar()
prikazi_lozinku = tk.StringVar()
prikazi_lozinku.set("prikazi")
lozinka_var = tk.StringVar()
duzina_lozinke = tk.IntVar()
duzina_lozinke.set(10)


# FUNKCIJE


def set_duzina_lozinke(value):
    duzina_lozinke.set(int(value))


def set_prikaz_lozinke():
    if prikazi_lozinku == "prikazi":
        ent_lozinka.config(show="")
    else:
        ent_lozinka.config(show="*")


def generiraj_lozinku():
    broj_znakova = duzina_lozinke.get()
    lozinka = ""

    for znak in range(broj_znakova):
        if slova_var.get():
            kompleksnost = random.choice([(65, 90), (97, 122)])
        elif brojevi_var.get():
            kompleksnost = random.choice([(48, 57)])
        elif spec_znakovi_var.get():
            kompleksnost = random.choice([(33, 47), (58, 64), (91, 96)])
        else:
            kompleksnost = random.choice([(33, 122)])

        random_broj = random.randint(*kompleksnost)
        znak = chr(random_broj)
        lozinka += znak

    lozinka_var.set(lozinka)


def resetiraj_lozinku():
    lozinka_var.set("")


def kopiraj_lozinku():
    root.clipboard_clear()
    root.clipboard_append(lozinka_var.get())


# ELEMENTI GUI-A
frm_postavke = tk.Frame(root).grid(column=0, columnspan=3, row=0, rowspan=3)

lbl_frm_postavke = tk.LabelFrame(frm_postavke, text="Postavke")
lbl_frm_postavke.columnconfigure((0, 1, 2), weight=1, minsize=90)
lbl_frm_postavke.grid(column=0, columnspan=3, row=0, padx=10, pady=10)

# -- -- Checkbox
ch_box_slova = tk.Checkbutton(lbl_frm_postavke, text="Slova", variable=slova_var).grid(
    column=0, row=0
)
ch_box_brojevi = tk.Checkbutton(
    lbl_frm_postavke, text="Brojevi", variable=brojevi_var
).grid(column=1, row=0)
ch_box_spec_znakovi = tk.Checkbutton(
    lbl_frm_postavke, text="Posebni znakovi", variable=spec_znakovi_var
).grid(column=2, row=0)

# -- -- Radiobuttons
rb_prikazi_lozinku = tk.Radiobutton(
    lbl_frm_postavke,
    text="Prikazi generiranu lozinku",
    variable=prikazi_lozinku,
    value="prikazi",
    command=set_prikaz_lozinke,
).grid(column=0, row=1)
rb_sakrij_lozinku = tk.Radiobutton(
    lbl_frm_postavke,
    text="Sakrij generiranu lozinku",
    variable=prikazi_lozinku,
    value="sakrij",
    command=set_prikaz_lozinke,
).grid(column=2, row=1)

# -- -- Klizac za duzinu lozinke
klizac_duzina = tk.Scale(
    lbl_frm_postavke,
    orient="horizontal",
    variable=duzina_lozinke,
    length=300,
    from_=8,
    to=40,
    command=set_duzina_lozinke,
)
klizac_duzina.grid(column=0, columnspan=3, row=2)

# Gumbi
frm_action_butttons = tk.Frame(root).grid(
    column=0, columnspan=3, row=3, padx=10, pady=10
)

btn_generiraj = tk.Button(
    frm_action_butttons, text="Generiraj lozinku", command=generiraj_lozinku
)
btn_generiraj.grid(column=0, row=3)

btn_kopiraj = tk.Button(
    frm_action_butttons, text="Kopiraj lozinku", command=kopiraj_lozinku
)
btn_kopiraj.grid(column=1, row=3)

btn_resetiraj = tk.Button(
    frm_action_butttons, text="Resetiraj", command=resetiraj_lozinku
)
btn_resetiraj.grid(column=2, row=3)


# Label Display
frm_display_gen_pass = tk.Frame(root).grid(
    column=0, columnspan=3, row=4, rowspan=2, padx=10, pady=10
)
lbl_pass = tk.Label(
    frm_display_gen_pass, text="Generirana lozinka", font=("Segoe UI", 14)
)
lbl_pass.grid(column=0, columnspan=3, row=4)

# Entry Display
ent_lozinka = tk.Entry(
    frm_display_gen_pass,
    textvariable=lozinka_var,
    justify="center",
    font=("Segoe UI", 16),
    width=30,
    background="SystemButtonFace",
    foreground="black",
    bd=0,
)
ent_lozinka.grid(column=0, columnspan=3, row=5, padx=15, pady=15)


root.mainloop()
