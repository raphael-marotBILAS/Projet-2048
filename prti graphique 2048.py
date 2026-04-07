import tkinter as tk
from tkinter import messagebox

# ===== Fonctions =====

def play():
    print("Début de la partie")

def left():
    print("Gauche")

def right():
    print("Droite")

def up():
    print("Haut")

def down():
    print("Bas")

def save():
    print("Sauvegarde")

def load():
    print("Chargement")

def quitter():
    score = 0  # à modifier plus tard
    messagebox.showinfo("Fin", "Score : " + str(score))
    fenetre.destroy()

# ===== Fenêtre =====

fenetre = tk.Tk()
fenetre.title("2048")
fenetre.geometry("400x400")

# ===== Frame pour les boutons =====

frame = tk.Frame(fenetre)
frame.pack(pady=20)

# Ligne 1
btn_play = tk.Button(frame, text="Play", command=play, width=10)
btn_play.grid(row=0, column=0, padx=5, pady=5)

btn_save = tk.Button(frame, text="Save", command=save, width=10)
btn_save.grid(row=0, column=1, padx=5, pady=5)

btn_load = tk.Button(frame, text="Load", command=load, width=10)
btn_load.grid(row=0, column=2, padx=5, pady=5)

# Flèches
btn_up = tk.Button(frame, text="↑", command=up, width=10)
btn_up.grid(row=1, column=1, padx=5, pady=5)

btn_left = tk.Button(frame, text="←", command=left, width=10)
btn_left.grid(row=2, column=0, padx=5, pady=5)

btn_down = tk.Button(frame, text="↓", command=down, width=10)
btn_down.grid(row=2, column=1, padx=5, pady=5)

btn_right = tk.Button(frame, text="→", command=right, width=10)
btn_right.grid(row=2, column=2, padx=5, pady=5)

# Quitter
btn_quit = tk.Button(frame, text="Exit", command=quitter, width=10)
btn_quit.grid(row=3, column=1, pady=10)

# ===== Lancement =====

fenetre.mainloop()
