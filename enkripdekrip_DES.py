import streamlit as st
import DES

def pad_message(message):
    while len(message) % 8 != 0:
        message += ' '
    return message

def generate_key(key):
    return DES.new(key, DES.MODE_ECB)

def encrypt_message(text, cipher):
    padded_text = pad_message(text)
    encrypted_text = cipher.encrypt(padded_text.encode('utf-8'))
    return encrypted_text

def decrypt_message(encrypted_text, cipher):
    decrypted_text = cipher.decrypt(encrypted_text)
    return unpad(decrypted_text, 8).decode('utf-8')

def main():
    st.title("🔑 ## DES Cryptography 🔑")

    with st.expander("Lebih lanjut mengenai DES!"):
        st.markdown(
            """
            DES adalah salah satu dari contoh Algoritma kriptografi modern.
            \nDES Merupakan data dienkripsi dalam blok 64-bit menggunakan kunci internal 56-bit 
            yang dibangkitkan dari kunci eksternal 64-bit.
            """
        )

    col1, col2 = st.columns(2)

    # Enkripsi pesan
    with col1:
        with st.form(key="encrypt"):
            st.subheader(f"Masukkan kalimat untuk dienkripsi:")
            key = st.text_input("Masukkan kunci 8 karakter:")
            if len(key) != 8:
                st.warning("Masukkan kunci dengan maksimal 8 karakter (contoh: 00000000)")
                st.stop()

            cipher = generate_key(key)

        text = st.text_area("Enter a message")
        submit = st.form_submit_button(label="Encrypt")

        if text == "":
            st.warning("!!Kotak enkripsi pesan tidak boleh kosong!!")

        if submit:
            try:
                encrypted_message = encrypt_message(text, cipher)
                st.write("Encrypted message: ", encrypted_message.hex())
            except:
                st.warning("Message too large, please enter a smaller message or use a larger key.")

    # Dekripsi pesan
    with col2:
        with st.form(key="decrypt"):
            st.subheader("Decrypt a message")
            encrypted_message_input = st.text_area("Enter encrypted message")
            submit1 = st.form_submit_button(label="Decrypt")

        if encrypted_message_input == "":
            st.warning("Please enter a message to decrypt")

        try:
            if submit1:
                decrypted_message = decrypt_message(bytes.fromhex(encrypted_message_input), cipher)
                st.write("Decrypted message: ", decrypted_message)
        except:
            st.warning("Please enter a valid encrypted message.")

    st.info("Setiap kali melakukan enkripsi, key akan digenerate secara otomatis. Silakan copy private key untuk melakukan dekripsi.")

    st.write("Kelompok 7 DES Kriptografi © 2023")

if __name__ == "__main__":
    main()
