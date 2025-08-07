## 🛡️ CryptX - Projet de Cryptographie en Python - V.0.2

<p align="center">
  <a href="https://developing-draw-3a8.notion.site/23d4c7b38e608098a12ae04bac41f98f?v=23d4c7b38e6080d78566000ca677c614&pvs=74">
    <img src="https://img.shields.io/badge/📋_Roadmap-Notion-000000?style=for-the-badge&logo=notion&logoColor=white&labelColor=2F3437" alt="Roadmap Notion" />
  </a>
  &nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/yoan-blochet">
    <img src="https://img.shields.io/badge/🤝_Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0A66C2" alt="LinkedIn Profile" />
  </a>
</p>

---

Ce projet personnel implémente plusieurs algorithmes classiques de **chiffrement/déchiffrement** en Python.
M'intéressant à la cryptographie et à la programmation, j’ai souhaité m’amuser en créant ce petit projet. Il est encore loin d’être complet, et je compte bien le compléter et le complexifier dans le futur.

---

## 🗂️ Fonctionnalités

Le programme permet d'appliquer plusieurs méthodes de chiffrement/déchiffrement :

### 1. 🔁 Chiffrement César
- Basé sur un décalage simple de caractères.
- Deux modes :
  - **ASCII 128** : utilise tous les caractères ASCII (peut produire des caractères invisibles).
  - **ASCII Imprimable** : limite aux 95 caractères visibles (ASCII 32 à 126 inclus).
- Supporte lecture/écriture depuis ou vers un fichier texte.

### 2. 🔑 Chiffrement de Vigenère
- Chiffrement par clé (texte).
- Deux versions :
  - **ASCII 128**
  - **ASCII Imprimable**
- Supporte :
  - lecture du texte depuis un fichier
  - import/export de la clé depuis un fichier texte (clair ou chiffré)
  - écriture du résultat dans un fichier

### 3. 🎲 Substitution Aléatoire
- Génère une clé aléatoire de substitution (bijective* sur les caractères imprimables).
- Permet le chiffrement et déchiffrement en inversant la clé.
- Supporte :
  - lecture du texte depuis un fichier
  - import/export de la clé depuis un fichier texte (clair ou chiffré)
  - écriture du résultat dans un fichier

<sup>*</sup> *Oui, je suis un matheux* 😉

---

### 🧑‍💻 Lancer le programme

```bash
python main.py
```

---

### ⌨️ Exemple d'utilisation

```
🔐 Menu Cryptographie
1. Chiffrement César
2. Chiffrement Vigenère
3. Substitution aléatoire
4. Quitter
Votre choix : 1
Lire le texte depuis un fichier (o/n) : o
Chemin du fichier texte : test.txt
Décalage (entier positif ou négatif) : 8 
Déchiffrer (o/n) : n
Utiliser seulement les caractères imprimables (o/n) : n
Résultat : Jwvrw}z(è(|w}{()
Sauvegarder le résultat dans un fichier (o/n) : o
Chemin du fichier de sortie : encrypted.txt
```

---

### 📦 Structure du projet

```
.
├── main.py                  # Point d'entrée (le fichier à éxécuter)
├── menu.py                  # Menus principaux interactif (console)
├── utils.py                 # Fonctions utilitaires (lecture/écriture, validation, etc.)
├── ciphers/                 # Contient toutes les fonctions de chiffrement/déchiffrement
│   └── substitution.py      # Fonctions de chiffrement/déchiffrement par substitution
└── README.md                # Le fichier que vous lisez 😆
```

---

### 📆 Améliorations futures

* Nouvelles options de chiffrement **Base64** (oui je sais, c'est pas vraiment du chiffrement, mais de l'encodage), **XOR**...
* Commencer à jouer avec les maths pour chiffrer/déchiffrer des données...
* Hashage de texte et/ou fichier.
* Analyse & attaques pour decrypter les messages chiffrés (analyse fréquentielle; brute force, Test de Kasiski...).
* Interface graphique (UI dans une version future 😉).

Pour suivre la roadmap complète du projet et son évolution :

[Roadmap du projet (Notion)](https://developing-draw-3a8.notion.site/23d4c7b38e608098a12ae04bac41f98f?v=23d4c7b38e6080d78566000ca677c614&pvs=74)

---

### 🎓 Auteur

Projet réalisé par **Yoan Blochet**, étudiant en 1ère année du cycle ingénieur à l'ISAE‑ENSMA (Promotion 2028).

---

### 🔒 Licence
Ce projet est sous licence MIT – Voir le fichier [LICENSE](LICENSE).

---
