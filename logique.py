import random
from config import TAILLE

def compresser(ligne):
    nouvelle = [x for x in ligne if x != 0]
    return nouvelle + [0] * (TAILLE - len(nouvelle))

def fusionner(ligne):
    [span_1](start_span)"""Fusionne les tuiles selon les règles du projet[span_1](end_span)."""
    for i in range(TAILLE - 1):
        if ligne[i] == ligne[i+1] and ligne[i] != 0:
            ligne[i] *= 2
            ligne[i+1] = 0
    return ligne

def tourner(grille):
    return [list(row) for row in zip(*grille[::-1])]

def ajouter_tuile(grille):
    [span_2](start_span)"""Le joueur 'tuile' place un 2 (90%) ou un 4 (10%)[span_2](end_span)."""
    cases_vides = [(i, j) for i in range(TAILLE) for j in range(TAILLE) if grille[i][j] == 0]
    if cases_vides:
        i, j = random.choice(cases_vides)
        grille[i][j] = 2 if random.random() < 0.9 else 4
    return grille
  
