####################### VERIFICATION DES ENTREES UTILISATEUR #######################

def ask_yes_no(question):
    while True:
        answer = input(question + " (o/n) : ").lower()
        if answer in ["o", "n"]:
            return answer == "o"
        print("Réponse invalide. Tapez 'o' ou 'n'.")

def ask_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Veuillez entrer un entier valide.")

def safe_read_file(prompt):
    while True:
        path = input(prompt)
        try:
            return read_file(path)
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier : {e}")

def safe_write_file(prompt, content):
    while True:
        path = input(prompt)
        try:
            write_file(path, content)
            return
        except Exception as e:
            print(f"Erreur lors de l'écriture du fichier : {e}")

def ask_non_empty(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Ce champ ne peut pas être vide.")


########################### LECTURE/ECRITURE DE FICHIERS ###########################


def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
