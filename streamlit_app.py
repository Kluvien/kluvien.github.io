import streamlit as st
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key

# Generate keys
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    pem_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    pem_public_key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return pem_private_key, pem_public_key

# Encrypt function
def encrypt_message(message, public_key):
    public_key = load_pem_public_key(public_key, backend=default_backend())
    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

# Decrypt function
def decrypt_message(encrypted, private_key):
    private_key = load_pem_private_key(private_key, password=None, backend=default_backend())
    original_message = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return original_message.decode()

# Streamlit UI
st.title('RSA Encryption and Decryption')

with st.form("my_form"):
    message = st.text_input("Enter a message to encrypt")
    submit_button = st.form_submit_button("Encrypt")

if submit_button:
    pem_private_key, pem_public_key = generate_keys()
    encrypted_message = encrypt_message(message, pem_public_key)
    st.write("Encrypted:", encrypted_message)

    decrypted_message = decrypt_message(encrypted_message, pem_private_key)
    st.write("Decrypted:", decrypted_message)
