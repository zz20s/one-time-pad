import secrets
import string


def clean_text(text):
    """Remove spaces and convert to uppercase."""
    return text.replace(" ", "").upper()


def encrypt(message, key):
    result = ""

    for p, k in zip(message, key):
        p_value = ord(p) - ord("A")
        k_value = ord(k) - ord("A")

        c_value = (p_value + k_value) % 26
        result += chr(c_value + ord("A"))

    return result


def decrypt(ciphertext, key):
    result = ""

    for c, k in zip(ciphertext, key):
        c_value = ord(c) - ord("A")
        k_value = ord(k) - ord("A")

        p_value = (c_value - k_value) % 26
        result += chr(p_value + ord("A"))

    return result

def generate_key(length): 
    return "".join(
        secrets.choice(string.ascii_uppercase) 
        for _ in range(length)
    )