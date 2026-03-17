def bouton_load(nom_fichier="sauvegarde.txt"):
    nouvelle_grille = []
    try:
        with open(nom_fichier, "r") as f:
            for ligne in f:
                # On nettoie la ligne et on convertit les textes en entiers
                valeurs = ligne.strip().split(",")
                if valeurs:
                    nouvelle_grille.append([int(v) for v in valeurs])
        print("Partie chargée !")
        return nouvelle_grille
    except FileNotFoundError:
        print("Aucun fichier de sauvegarde trouvé.")
        return None

# Exemple d'utilisation :
# grille_chargee = bouton_load()