import csv
import random as rd
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()
root.title("Génerateur de Liste de Vocabulaire")
root.geometry("300x200")


def fileModify():
    filename = askopenfilename(parent=root, title="Ouvrir votre document", initialdir="/",
                               filetypes=[('csv files', '.csv'), ('all files', '.*')])
    data = []
    file = asksaveasfilename(title="Enregistrer sous...", filetypes=[("csv files", ".csv"), ("Tous", "*")], parent=root)
    tk.Label(root, text="Votre fichier a bien été créé, vous le trouverez à compléter").pack(padx=10, pady=10)
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=";")
        for row in spamreader:
            data.append(row)

    with open(file, 'w', newline='') as csvT:
        spamwriter = csv.writer(csvT, delimiter=',')
        for row in data:
            if row[2] == '' or row[3] == '':
                delete = rd.randint(0, 1)
                row[delete] = ''
            else:
                for y in range(0, 3, 2):
                    delete = rd.randint(0 + y, 1 + y)
                    row[delete] = ''
            spamwriter.writerow(row)


button = tk.Button(root, text="Cliquer ici pour ouvir un fichier", command=fileModify)
button.pack(pady=10)
root.mainloop()