from tkinter import *

# ------------------------
# Données du jeu (exemple)
# ------------------------
grid = [
    [2, 0, 4, 8],
    [0, 2, 4, 0],
    [0, 0, 2, 2],
    [4, 8, 16, 32]
]

score = 1200

# ------------------------
# Fonction SAVE
# ------------------------
def save_game(grid, score):
    file = open("save.txt", "w")

    file.write(str(score) + "\n")

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            file.write(str(grid[i][j]) + " ")
        file.write("\n")

    file.close()
    print("Partie sauvegardée")

# ------------------------
# Bouton SAVE
# ------------------------
def bouton_save():
    save_game(grid, score)

# ------------------------
# Interface
# ------------------------
root = Tk()
root.title("2048 - Test Save")

button_save = Button(root, text="Save", command=bouton_save)
button_save.pack(pady=20)

root.mainloop()