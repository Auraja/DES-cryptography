import streamlit as st
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

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

    st.markdown(
            """
            DES adalah salah satu dari contoh Algortima kriptografi modern.
            \nDES Merupakan data dienkripsi dalam blok 64-bit menggunakan kunci internal 56-bit yang dibangkitkan dari kunci eksternal 64-bit.
            """
        )

    key = st.text_input("Masukkan kunci 8 karakter:")

    if len(key) != 8:
        st.warning("Masukkan kunci dengan maksimal 8 karakter (contoh : 00000000)")
        st.stop()

    pilihan = st.selectbox("Pilih opsi kriptografi : ", ["Enkripsi", "Dekripsi"])
    st.warning(f"Opsi yang dipilih: {pilihan}")

    if pilihan == "Enkripsi":
        message = st.text_area(f"Masukkan kalimat untuk di{pilihan.lower()}:")

        if st.button(f"{pilihan}"):
            key_bytes = key.encode('utf-8')

            if pilihan == "Enkripsi":
                result = des_encrypt(message, key_bytes)
                st.success(f"{pilihan} berhasil.")
                st.text(f"Pesan {pilihan} :")
                st.text(result)
    else:
        if st.button(f"{pilihan}"):
            key_bytes = key.encode('utf-8')

            if pilihan == "Dekripsi":
                hasil = des_decrypt(message, key_bytes)
                st.success(f"{pilihan} berhasil.")
                st.text(f"Pesan {pilihan} :")
                st.text(hasil)
            
    st.write("""## Projek Kelompok Kriptografi 7
                    1. Hanifah Az-zahra        2210511046
                    2. Dinda Cantika Putri     2210511054
                    3. Ika Kusuma W.           2210511058
                    4. Muhammad Alif Nadin     2210511067
                    5. Derajat Salim W.        22105110??
             """)
if __name__ == "__main__":
    main()
