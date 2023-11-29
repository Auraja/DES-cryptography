import streamlit as st

def pad_message(message):
    while len(message) % 8 != 0:
        message += ' '
    return message

def initial_permutation(block):
    return block

def final_permutation(block):
    return block

def des_encrypt_block(block, key):
    return block

def des_decrypt_block(block, key):
    return block

def des_encrypt(plaintext, key):
    ciphertext = ""
    for i in range(0, len(plaintext), 8):
        block = initial_permutation(plaintext[i:i+8])
        encrypted_block = des_encrypt_block(block, key)
        ciphertext += final_permutation(encrypted_block)
    return ciphertext

def des_decrypt(ciphertext, key):
    plaintext = ""
    for i in range(0, len(ciphertext), 8):
        block = initial_permutation(ciphertext[i:i+8])
        decrypted_block = des_decrypt_block(block, key)
        plaintext += final_permutation(decrypted_block)
    return plaintext

def main():
    st.title("DES Encryption and Decryption")

    st.markdown(
        """
        DES adalah salah satu dari contoh Algoritma kriptografi modern.
        \nDES Merupakan data dienkripsi dalam blok 64-bit menggunakan kunci internal 56-bit yang dibangkitkan dari kunci eksternal 64-bit.
        """
    )

    key = st.text_input("Masukkan kunci 8 karakter:")

    if len(key) != 8:
        st.warning("Masukkan kunci dengan maksimal 8 karakter (contoh: 00000000)")
        st.stop()

    pilihan = st.selectbox("Pilih opsi kriptografi:", ["Enkripsi", "Dekripsi"])
    st.warning(f"Opsi yang dipilih: {pilihan}")

    message = st.text_area(f"Masukkan kalimat untuk di{pilihan.lower()}:")

    if st.button(f"{pilihan}"):
        key_bytes = key.encode('utf-8')

        if pilihan == "Enkripsi":
            result = des_encrypt(message, key_bytes)
            st.success(f"{pilihan} berhasil.")
            st.text(f"Pesan {pilihan} :")
            st.text(result)
        elif pilihan == "Dekripsi":
            result = des_decrypt(message, key_bytes)
            st.success(f"{pilihan} berhasil.")
            st.text(f"Pesan {pilihan} :")
            st.text(result)

    st.write("""## Projek Kelompok 
            1. Hanifah Az-zahra
        2. Dinda Cantika Putri
        3. Ika Kusuma W.
        4. M. Alif Nadin Putra      22105110
        5. Derajat Salim Wibowo     22105110??
            """)

if __name__ == "__main__":
    main()
