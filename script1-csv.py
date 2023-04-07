import csv

# Ouverture du fichier CSV en mode lecture
with open('fichier1.csv', 'r') as csvfile:
    # Création d'un objet DictReader pour lire le fichier CSV
    reader = csv.DictReader(csvfile)
    
    # Définition des colonnes à extraire
    colonnes_a_extraire = ['NAMESPACE', 'NAME', 'SCHEDULE']
    
    # Ouverture du fichier de sortie en mode écriture
    with open('fichier_sortie.csv', 'w', newline='') as outfile:
        # Création d'un objet DictWriter pour écrire dans le fichier de sortie
        writer = csv.DictWriter(outfile, fieldnames=colonnes_a_extraire)

        # Écriture de l'en-tête du fichier de sortie
        writer.writeheader()

        # Boucle sur chaque ligne du fichier d'entrée
        for row in reader:
            # Extraction des colonnes spécifiées
            new_row = {colonne: row[colonne] for colonne in colonnes_a_extraire}

            # Écriture de la ligne extraite dans le fichier de sortie
            writer.writerow(new_row)

