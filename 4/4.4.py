from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64

# ================= SHA-256 =================
def hash_string(message: str) -> str:
    """Обчислення SHA-256 гешу"""
    return sha256(message.encode('utf-8')).hexdigest()

# ================= AES =================
def pad(message: str) -> bytes:
    """Паддинг для AES (16 байт)"""
    data = message.encode('utf-8')
    pad_len = 16 - len(data) % 16
    return data + bytes([pad_len] * pad_len)

def unpad(data: bytes) -> str:
    """Видалення паддингу"""
    pad_len = data[-1]
    return data[:-pad_len].decode('utf-8')

def aes_encrypt(key: str, message: str):
    """Шифрування AES-CBC"""
    key_bytes = key[:32].encode('utf-8')  # 256-бітний ключ
    cipher = AES.new(key_bytes, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

def aes_decrypt(key: str, iv: str, ct: str):
    """Розшифрування AES-CBC"""
    key_bytes = key[:32].encode('utf-8')
    iv_bytes = base64.b64decode(iv)
    ct_bytes = base64.b64decode(ct)
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    pt = unpad(cipher.decrypt(ct_bytes))
    return pt

# ================= RSA =================
def generate_rsa_keys():
    """Генерація пари RSA ключів"""
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def sign_message(private_key_bytes: bytes, message: str) -> str:
    """Цифровий підпис повідомлення"""
    key = RSA.import_key(private_key_bytes)
    h = SHA256.new(message.encode('utf-8'))
    signature = pkcs1_15.new(key).sign(h)
    return base64.b64encode(signature).decode('utf-8')

def verify_signature(public_key_bytes: bytes, message: str, signature_b64: str) -> bool:
    """Перевірка цифрового підпису"""
    key = RSA.import_key(public_key_bytes)
    h = SHA256.new(message.encode('utf-8'))
    signature = base64.b64decode(signature_b64)
    try:
        pkcs1_15.new(key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

# ================= DEMO =================
if __name__ == "__main__":
    message = "Привіт, це секретне повідомлення!"
    password = "mysecretpassword"

    print("=== Гешування SHA-256 ===")
    hashed = hash_string(message)
    print("SHA-256 геш:", hashed)

    print("\n=== Симетричне шифрування AES ===")
    iv, ciphertext = aes_encrypt(password, message)
    print("AES шифр:", ciphertext)
    decrypted = aes_decrypt(password, iv, ciphertext)
    print("AES розшифровано:", decrypted)

    print("\n=== RSA: цифровий підпис ===")
    priv_key, pub_key = generate_rsa_keys()
    signature = sign_message(priv_key, message)
    print("Цифровий підпис:", signature)
    verified = verify_signature(pub_key, message, signature)
    print("Підпис вірний:", verified)

    print("\n=== Різниця між гешуванням і шифруванням ===")
    print("- Гешування: одностороннє, неможливо відновити початкове повідомлення.")
    print("- Шифрування: двостороннє, можна розшифрувати за допомогою ключа.")