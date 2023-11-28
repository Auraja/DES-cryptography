import streamlit as st
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def pad_message(message):
    # Pad the message with spaces to make its length a multiple of 8
    while len(message) % 8 != 0:
        message += ' '
    return message

def des_encrypt(key, message):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_message = pad_message(message)
    encrypted_message = cipher.encrypt(padded_message.encode('utf-8'))
    return encrypted_message

def des_decrypt(key, encrypted_message):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_message = cipher.decrypt(encrypted_message).decode('utf-8').rstrip()
    return decrypted_message

def main():
    st.title("DES Encryption and Decryption")

    key = st.text_input("Enter 8-character key:")

    if len(key) != 8:
        st.warning("Please enter a valid 8-character key.")
        st.stop()

    message = st.text_area("Enter message:")

    encrypt_button = st.button("Encrypt")
    decrypt_button = st.button("Decrypt")

    if encrypt_button:
        key_bytes = key.encode('utf-8')
        encrypted_message = des_encrypt(key_bytes, message)
        st.success("Encryption successful:")
        st.text("Encrypted Message:")
        st.text(encrypted_message)

    if decrypt_button:
        key_bytes = key.encode('utf-8')
        decrypted_message = des_decrypt(key_bytes, message.encode('utf-8'))
        st.success("Decryption successful:")
        st.text("Decrypted Message:")
        st.text(decrypted_message)

if __name__ == "__main__":
    main()
