
import random

############################# CHIFFRAGE CESAR #############################

def encrypt_caesar_ASCII_128(text, shift):
    """
    Encryptage César ASCII 128 (version améliorée du chiffrage césar classique avec les 128 caractères de la table ASCII)
    ATTENTION CETTE VERSION PEUT RENVOYER DES CARACTERES NON IMPRIMABLE (non visible avec print)
    """

    result = ""
    for char in text:
        result += chr((ord(char) + shift))
    return result

def encrypt_caesar_ASCII_printable(text, shift):
    """
    Encryptage César ASCII imprimable (pouvant utiliser les 95 caractères imprimables de la table ASCII)
    Tout caractère non imprimable est laissé inchangé.
    """

    result = ""
    printable_min = 32
    printable_max = 126
    printable_range = printable_max - printable_min + 1  # les 95 caractères imprimables

    for char in text:
        char_code = ord(char)
        if printable_min <= char_code <= printable_max:
            result += chr((char_code - printable_min + shift) % printable_range + printable_min)
        else:
            result += char  # on garde les caractères non imprimables (ex: \n)
    
    return result

def decrypt_caesar_ASCII_128(text, shift):
    """
    Décryptage du texte encrypté par chiffrage César ASCII 128
    """

    return encrypt_caesar_ASCII_128(text, -shift)

def decrypt_caesar_ASCII_printable(text, shift):
    """
    Décryptage du texte encrypté par chiffrage César ASCII Imprimable
    """

    return encrypt_caesar_ASCII_printable(text, -shift)


########################### CHIFFRAGE VIGENERE ############################

def encrypt_vigenere_ASCII_128(text, key, is_decryption=False):
    """
    Encryptage Vigenère ASCII 128 (pouvant utiliser les 128 caractères de la table ASCII)
    ATTENTION CETTE VERSION PEUT RENVOYER DES CARACTERES NON IMPRIMABLE (non visible avec print)
    """

    result = ""
    i = 0
    for char in text:
        key_letter = key[i % len(key)] 
        if is_decryption:
            result += chr((ord(char) - ord(key_letter)) % 128)
        else:
            result += chr((ord(char) + ord(key_letter)) % 128)
        i += 1
    return result

def encrypt_vigenere_ASCII_printable(text, key, is_decryption=False):
    """
    Encryptage Vigenère ASCII imprimable (pouvant utiliser les 95 caractères imprimables de la table ASCII)
    Tout caractère non imprimable est laissé inchangé.
    """

    result = ""
    i = 0
    printable_min = 32
    printable_max = 126
    printable_range = printable_max - printable_min + 1  # les 95 caractères imprimables

    for char in text:
        char_code = ord(char)
        if printable_min <= char_code <= printable_max:
            key_letter = key[i % len(key)] 
            key_code = ord(key_letter)
            if is_decryption:
                result += chr((char_code - printable_min - key_code) % printable_range + printable_min)
            else:
                result += chr((char_code - printable_min + key_code) % printable_range + printable_min)
            i += 1
        else:
            result += char  # Pas touche aux caractères non imprimables si présent
    return result

def decrypt_vigenere_ASCII_128(text, key):
    """
    Décryptage du texte encrypté par chiffrage Vigenère ASCII 128
    """

    return encrypt_vigenere_ASCII_128(text, key, True)

def decrypt_vigenere_ASCII_128(text, key):
    """
    Décryptage du texte encrypté par chiffrage Vigenère ASCII Imprimable
    """

    return encrypt_vigenere_ASCII_printable(text, key, True)


######################### SUBSTITUTION ALEATOIRE ##########################

def generate_substitution_key():
    """
    Génère aléatoirement la clé de chiffrement :
    un dictionnaire de correspondances 2 à 2 avec tous les (95) caractères ASCII imprimables.
    """

    alphabet = [chr(i) for i in range(32, 127)]
    shuffled = alphabet[:]
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))  # clé de chiffrement

def invert_key(key):
    """
    Inverse le dictionnaire (i.e. la clé) de chiffrement qui devient alors le dictionnaire (i.e. la clé) de déchiffrement
    """

    return {v: k for k, v in key.items()}  # clé de déchiffrement

def substitute(text, key):
    """
    Réalise la substitution aléatoire en utilisant le dictionnaire de chiffrement (liant un caractère à un autre)
    """

    result = ""
    for char in text:
        result += key.get(char, char)  # Remplace si trouvé, sinon garde le char original
    return result
