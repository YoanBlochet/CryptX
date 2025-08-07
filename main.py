from menu import caesar_menu, vigenere_menu, substitution_menu

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
