from ciphers.substitution import *
from utils import *
import json

# Vous remarquerez que j'ai pas mal documenté les fonctions de ce fichier (la gestion des menus en gros).
# J'ai trouvé que c'était une bonne idée vu la longueur des fonctions (bien qu'elles ne soient pas très complexes).

def caesar_menu():
    """
    Menu Chiffrement César (si option choisie)
    """

    # Demande si l'utilisateur veut lire le texte depuis un fichier
    use_file = ask_yes_no("Lire le texte depuis un fichier")
    text = safe_read_file("Chemin du fichier texte : ") if use_file else ask_non_empty("Texte : ")

    # Demande le décalage pour le chiffrement César
    shift = ask_int("Décalage (entier positif ou négatif) : ")

    # Chiffrement ou déchiffrement ?
    decrypt = ask_yes_no("Déchiffrer")

    # Uniquement les caractères imprimables ou toute la table ASCII ?
    printable = ask_yes_no("Utiliser seulement les caractères imprimables")

    # On applique le bon algorithme selon les choix de l'utilisateur
    result = (
        decrypt_caesar_ASCII_printable(text, shift) if decrypt else encrypt_caesar_ASCII_printable(text, shift)
    ) if printable else (
        decrypt_caesar_ASCII_128(text, shift) if decrypt else encrypt_caesar_ASCII_128(text, shift)
    )

    # Oui, je suis devenu un fan de l'écriture compacte :)

    print("Résultat :", result)

    # Propose de sauvegarder le résultat dans un fichier
    if ask_yes_no("Sauvegarder le résultat dans un fichier"):
        safe_write_file("Chemin du fichier de sortie : ", result)

def vigenere_menu():
    """
    Menu Chiffrement Vigenère (si option choisie)
    """
    
    # Demande si l'utilisateur veut lire le texte depuis un fichier
    use_file = ask_yes_no("Lire le texte depuis un fichier")
    text = safe_read_file("Chemin du fichier texte : ") if use_file else ask_non_empty("Texte : ")

    # Clé fournie depuis un fichier ou entrée manuelle ?
    key_from_file = ask_yes_no("Lire la clé depuis un fichier")
    key = (
        safe_read_file("Chemin du fichier contenant la clé : ").strip()
        if key_from_file else ask_non_empty("Clé (texte) : ")
    )

    # Chiffrement ou déchiffrement ?
    decrypt = ask_yes_no("Déchiffrer")

    # Uniquement les caractères imprimables ou toute la table ASCII ?
    printable = ask_yes_no("Utiliser seulement les caractères imprimables")

    # On applique le bon algorithme selon les choix de l'utilisateur
    result = (
        encrypt_vigenere_ASCII_printable(text, key, is_decryption=decrypt)
        if printable else
        encrypt_vigenere_ASCII_128(text, key, is_decryption=decrypt)
    )

    print("Résultat :", result)

    # Propose de sauvegarder le résultat dans un fichier
    if ask_yes_no("Sauvegarder le résultat dans un fichier"):
        safe_write_file("Chemin du fichier de sortie : ", result)

def substitution_menu():
    """
    Menu Chiffrement par Substitution Aléatoire (si option choisie)
    """

    # Chiffrement ou déchiffrement ?
    decrypt = ask_yes_no("Déchiffrer")

    # Demande si l'utilisateur veut lire le texte depuis un fichier
    use_file = ask_yes_no("Lire le texte depuis un fichier")
    text = safe_read_file("Chemin du fichier texte : ") if use_file else ask_non_empty("Texte : ")

    key = None  # Initialisation de la variable de clé

    # Clé chargée depuis un fichier JSON (JSON parce que plus simple pour la gestion de dicos) ?
    if ask_yes_no("Charger une clé depuis un fichier JSON"):
        while True:
            key_path = input("Chemin du fichier JSON : ")
            try:
                with open(key_path, "r", encoding="utf-8") as f:
                    key = json.load(f)
                break
            except Exception as e:
                print(f"Erreur lors du chargement : {e}")
    
    elif decrypt:
        # Impossible de déchiffrer sans clé : on bloque
        print("Impossible de déchiffrer sans clé existante. Veuillez charger une clé JSON.")
        return

    else:
        # Si chiffrement sans clé fournie : on en génère une
        print("\nGénération d'une nouvelle clé de substitution...")
        key = generate_substitution_key()
        print("Clé de chiffrement générée :", key)

        # Propose à l'utilisateur de sauvegarder la clé dans un fichier JSON (encore une fois, .JSON parce que plus simple pour la gestion de dicos)
        if ask_yes_no("Sauvegarder la clé dans un fichier JSON"):
            while True:
                key_path = input("Chemin du fichier JSON : ")
                try:
                    with open(key_path, "w", encoding="utf-8") as f:
                        json.dump(key, f)
                    break
                except Exception as e:
                    print(f"Erreur : {e}")

    # Si on veut déchiffrer, il faut inverser la clé de substitution
    if decrypt:
        key = invert_key(key)

    # Application du chiffrement ou déchiffrement avec la clé choisie
    result = substitute(text, key)
    print("\nRésultat :", result)

    # Propose de sauvegarder le résultat dans un fichier
    if ask_yes_no("Sauvegarder le résultat dans un fichier"):
        safe_write_file("Chemin du fichier de sortie : ", result)
