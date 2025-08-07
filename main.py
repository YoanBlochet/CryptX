from ciphers.substitution import *

def caesar_menu():
    text = input("Texte : ")
    shift = int(input("Décalage (entier positif ou négatif) : "))
    decrypt = input("Déchiffrer ? (o/n) : ").lower() == "o"
    printable = input("Utiliser seulement les caractères imprimables ? (o/n) : ").lower() == "o"

    if printable:
        if decrypt:
            result = decrypt_caesar_ASCII_printable(text, shift)
        else:
            result = encrypt_caesar_ASCII_printable(text, shift)
    else:
        if decrypt:
            result = decrypt_caesar_ASCII_128(text, shift)
        else:
            result = encrypt_caesar_ASCII_128(text, shift)

    print("Résultat :", result)

def vigenere_menu():
    text = input("Texte : ")
    key = input("Clé (texte) : ")
    decrypt = input("Déchiffrer ? (o/n) : ").lower() == "o"
    printable = input("Utiliser seulement les caractères imprimables ? (o/n) : ").lower() == "o"

    if printable:
        result = encrypt_vigenere_ASCII_printable(text, key, is_decryption=decrypt)
    else:
        result = encrypt_vigenere_ASCII_128(text, key, is_decryption=decrypt)

    print("Résultat :", result)

def substitution_menu():
    text = input("Texte à chiffrer : ")
    key = generate_substitution_key()
    print("Clé de chiffrement générée :", key)

    encrypted = substitute(text, key)
    print("Texte chiffré :", encrypted)

    decrypt_key = invert_key(key)
    decrypted = substitute(encrypted, decrypt_key)
    print("Texte déchiffré (avec clé inversée) :", decrypted)

def main():
    while True:
        print("\n🔐 Menu Cryptographie")
        print("1. Chiffrement César")
        print("2. Chiffrement Vigenère")
        print("3. Substitution aléatoire")
        print("4. Quitter")
        choice = input("Votre choix : ")

        if choice == "1":
            caesar_menu()
        elif choice == "2":
            vigenere_menu()
        elif choice == "3":
            substitution_menu()
        elif choice == "4":
            print("À bientôt !")
            break
        else:
            print("Choix invalide. Réessayez.")

if __name__ == "__main__":
    main()
